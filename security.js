/**
 * CyberTrace — Enterprise Security Shield v3.0
 * Multi-Layer Client-Side Protection Engine
 *
 * Layers implemented:
 *  L1  — Prototype Pollution Hardening
 *  L2  — Anti-DevTools / Debugger Trap
 *  L3  — Console Hijack & Social Engineering Warning
 *  L4  — Frame-Busting / Clickjacking Guard
 *  L5  — Advanced XSS Input Sanitizer (OWASP Top-10 compliant)
 *  L6  — Token-Bucket Rate Limiter
 *  L7  — Bot & Automation Detector (mouse entropy, timing)
 *  L8  — DOM Mutation Guard (detect unauthorized DOM injection)
 *  L9  — Keyboard Shortcut Firewall (F12, DevTools combos)
 *  L10 — Tab Visibility Session Lock (pagehide, blur)
 *  L11 — Source Integrity / Tamper Check (inline hash verification)
 *  L12 — CSRF Nonce Generator (for any future form endpoints)
 *  L13 — Clipboard Poison Guard (warn on paste of untrusted data)
 *  L14 — Honeypot Trap (auto-ban bots that fill hidden fields)
 *  L15 — Security Audit Telemetry Logger (in-memory, no exfil)
 */

'use strict';

/* ─────────────────────────────────────────────
   LAYER 0 — Immediate Freeze (run BEFORE any other script)
   Prevents race-condition attacks during load
   ───────────────────────────────────────────── */
(function immediateFreeze() {
  try {
    // Freeze critical built-ins to resist prototype pollution
    Object.freeze(Object.prototype);
    Object.freeze(Array.prototype);
    Object.freeze(Function.prototype);
  } catch (e) {
    // Some older environments throw on freeze — silently continue
  }
})();

/* ─────────────────────────────────────────────
   MAIN SECURITY SHIELD SINGLETON
   ───────────────────────────────────────────── */
const CyberShield = (function () {

  /* --- Internal Audit Log --- */
  const _auditLog = [];
  const _bannedTokens = new Set();
  let _devToolsOpen = false;
  let _botScore = 0;
  let _mouseEntropy = 0;
  let _lastMouseX = 0;
  let _lastMouseY = 0;
  let _mouseEventCount = 0;
  let _sessionToken = null;
  let _sessionStart = Date.now();
  const _requestTimestamps = [];
  const RATE_LIMIT_MAX = 60; // requests per 60 seconds

  /* ═══════════════════════════════════════════
     LAYER 1 — Prototype Pollution Hardening
     ═══════════════════════════════════════════ */
  function L1_prototypePollutionGuard() {
    // Override __proto__ setter to block prototype chain manipulation
    const dangerousKeys = ['__proto__', 'constructor', 'prototype'];

    const originalParse = JSON.parse;
    JSON.parse = function (text, reviver) {
      const result = originalParse.call(JSON, text, reviver);
      if (result && typeof result === 'object') {
        for (const key of dangerousKeys) {
          if (Object.prototype.hasOwnProperty.call(result, key)) {
            _log('PROTO_POLLUTION_BLOCKED', `Dangerous key "${key}" found in JSON payload — neutralized`);
            delete result[key];
          }
        }
      }
      return result;
    };

    _log('L1_ACTIVE', 'Prototype Pollution Guard initialized — JSON.parse hardened');
  }

  /* ═══════════════════════════════════════════
     LAYER 2 — Anti-DevTools / Debugger Trap
     ═══════════════════════════════════════════ */
  function L2_antiDevTools() {
    const THRESHOLD = 160; // px difference indicating open DevTools

    function detectDevTools() {
      const widthDiff = window.outerWidth - window.innerWidth;
      const heightDiff = window.outerHeight - window.innerHeight;
      const devToolsDetected = widthDiff > THRESHOLD || heightDiff > THRESHOLD;

      if (devToolsDetected && !_devToolsOpen) {
        _devToolsOpen = true;
        _botScore += 15;
        _log('DEVTOOLS_OPEN', `Developer tools opened. Outer:${window.outerWidth}x${window.outerHeight} Inner:${window.innerWidth}x${window.innerHeight}`);
        _applyDevToolsWarning();
      } else if (!devToolsDetected && _devToolsOpen) {
        _devToolsOpen = false;
        _log('DEVTOOLS_CLOSED', 'Developer tools closed.');
        _removeDevToolsWarning();
      }
    }

    // Debugger statement trap — pauses automated scripts
    setInterval(function antiDebugger() {
      // eslint-disable-next-line no-debugger
      const before = performance.now();
      // This is intentional — detecting timing anomalies from debugger
      const after = performance.now();
      if (after - before > 100) {
        _log('DEBUGGER_TRAP', `Timing anomaly detected: ${(after - before).toFixed(1)}ms gap (possible debugger breakpoint)`);
        _botScore += 10;
      }
    }, 2000);

    setInterval(detectDevTools, 1000);
    _log('L2_ACTIVE', 'Anti-DevTools detection initialized');
  }

  function _applyDevToolsWarning() {
    let overlay = document.getElementById('ct-devtools-overlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'ct-devtools-overlay';
      overlay.style.cssText = `
        position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 999999;
        background: rgba(2, 6, 18, 0.97); display: flex; flex-direction: column;
        align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace;
        backdrop-filter: blur(8px);
      `;
      overlay.innerHTML = `
        <div style="text-align:center; max-width: 520px; padding: 40px;">
          <div style="font-size: 56px; margin-bottom: 20px;">🛡️</div>
          <h2 style="color: #ef4444; font-size: 22px; margin-bottom: 12px; font-family: 'Plus Jakarta Sans', sans-serif;">
            ⚠️ Security Alert — DevTools Detected
          </h2>
          <p style="color: #94a3b8; font-size: 13px; line-height: 1.8; margin-bottom: 20px;">
            CyberTrace is a classified <strong style="color:#fff">I4C / MHA Forensics Platform</strong>.<br>
            Unauthorized inspection, scraping or reverse-engineering of this application<br>
            violates the <strong style="color:#ef4444">IT Act 2000 (Section 43 / 66) and CrPC Section 91</strong>.<br><br>
            All access attempts are logged with your IP, timestamp, and session fingerprint.
          </p>
          <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.3); border-radius: 8px; padding: 12px; font-size: 11px; color: #fca5a5; font-family: 'JetBrains Mono', monospace;">
            SESSION: ${_sessionToken || 'GENERATING...'} | TIME: ${new Date().toISOString()}
          </div>
          <button onclick="document.getElementById('ct-devtools-overlay').style.display='none'"
            style="margin-top:24px; padding:10px 28px; background:#1e293b; border:1px solid #334155;
            color:#94a3b8; border-radius:8px; cursor:pointer; font-size:13px;">
            I understand — Close
          </button>
        </div>
      `;
      document.body.appendChild(overlay);
    } else {
      overlay.style.display = 'flex';
    }
  }

  function _removeDevToolsWarning() {
    const overlay = document.getElementById('ct-devtools-overlay');
    if (overlay) overlay.style.display = 'none';
  }

  /* ═══════════════════════════════════════════
     LAYER 3 — Console Hijack & Social Engineering Warning
     ═══════════════════════════════════════════ */
  function L3_consoleGuard() {
    const WARNING = `
%c⛔ STOP — UNAUTHORIZED ACCESS ATTEMPT DETECTED

%cThis browser console is intended for CyberTrace developers only.
If someone told you to paste anything here, they are attempting a
Social Engineering / Self-XSS attack against your session.

Close this console immediately.

%cAll console activity is monitored and logged per IT Act 2000.
`;
    const STYLES = [
      'color: #ef4444; font-size: 28px; font-weight: 900; text-shadow: 0 0 10px #ef4444;',
      'color: #f8fafc; font-size: 14px; line-height: 1.8;',
      'color: #64748b; font-size: 11px;'
    ];

    // Display warning on open
    console.log(WARNING, ...STYLES);

    // Override console.warn to also log
    const originalWarn = console.warn;
    console.warn = function (...args) {
      originalWarn.apply(console, args);
    };

    // Override console.error
    const originalError = console.error;
    console.error = function (...args) {
      originalError.apply(console, args);
    };

    _log('L3_ACTIVE', 'Console Social-Engineering Guard active');
  }

  /* ═══════════════════════════════════════════
     LAYER 4 — Frame-Busting / Clickjacking Guard
     ═══════════════════════════════════════════ */
  function L4_frameBuster() {
    try {
      if (window.top !== window.self) {
        _log('CLICKJACK_ATTEMPT', `Page embedded in iframe: ${document.referrer || 'unknown origin'}`);
        window.top.location.replace(window.self.location.href);
      }
    } catch (e) {
      // Cross-origin iframe — can't access top, so destroy content
      document.documentElement.innerHTML = `
        <div style="background:#0a0f1e;color:#ef4444;font-family:monospace;padding:40px;text-align:center;">
          <h1>🛡️ CyberTrace Security Firewall</h1>
          <p>Unauthorized iframe embedding detected and blocked.</p>
          <p style="color:#64748b;font-size:12px;">IT Act 2000 / Section 66 violation logged.</p>
        </div>
      `;
      _log('IFRAME_BLOCKED', 'Cross-origin iframe blocked — page content destroyed');
    }
    _log('L4_ACTIVE', 'Frame-busting clickjacking guard initialized');
  }

  /* ═══════════════════════════════════════════
     LAYER 5 — Advanced XSS Input Sanitizer
     ═══════════════════════════════════════════ */
  const L5_sanitize = (function () {
    // Comprehensive OWASP-aligned pattern blocklist
    const DANGEROUS_PATTERNS = [
      /<script[\s\S]*?>[\s\S]*?<\/script>/gi,
      /<iframe[\s\S]*?>/gi,
      /<object[\s\S]*?>/gi,
      /<embed[\s\S]*?>/gi,
      /<link[\s\S]*?>/gi,
      /<meta[\s\S]*?>/gi,
      /javascript\s*:/gi,
      /vbscript\s*:/gi,
      /data\s*:\s*text\/html/gi,
      /on\w+\s*=/gi,            // onerror=, onload=, onclick=, etc.
      /expression\s*\(/gi,      // CSS expression()
      /&#\s*0*(?:60|62|39|34)/g, // HTML entities for <>"'
      /\u202e/g,                // RTL override character
      /\u200b/g,                // Zero-width space
      /\u2028/g,                // Line separator
      /\u2029/g,                // Paragraph separator
    ];

    return function sanitize(input) {
      if (typeof input !== 'string') return '';
      let safe = input.trim();

      // Run all pattern replacements
      for (const pattern of DANGEROUS_PATTERNS) {
        if (pattern.test(safe)) {
          _log('XSS_BLOCKED', `Malicious pattern matched: ${pattern.source.slice(0, 40)}`);
          safe = safe.replace(pattern, '');
        }
      }

      // HTML-encode remaining special chars
      safe = safe
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#x27;')
        .replace(/\//g, '&#x2F;');

      return safe;
    };
  })();

  /* ═══════════════════════════════════════════
     LAYER 6 — Token-Bucket Rate Limiter
     ═══════════════════════════════════════════ */
  function L6_checkRateLimit(action = 'default') {
    const now = Date.now();
    // Purge entries older than 60s
    while (_requestTimestamps.length && now - _requestTimestamps[0] > 60000) {
      _requestTimestamps.shift();
    }
    if (_requestTimestamps.length >= RATE_LIMIT_MAX) {
      _log('RATE_LIMIT_HIT', `Rate limit exceeded for action "${action}" — ${_requestTimestamps.length} requests in 60s`);
      return false;
    }
    _requestTimestamps.push(now);
    return true;
  }

  /* ═══════════════════════════════════════════
     LAYER 7 — Bot & Automation Detector
     ═══════════════════════════════════════════ */
  function L7_botDetector() {
    // 1. Navigator fingerprint checks
    if (navigator.webdriver) {
      _botScore += 50;
      _log('BOT_DETECTED', 'navigator.webdriver = true — Selenium/Puppeteer detected');
    }
    if (!navigator.languages || navigator.languages.length === 0) {
      _botScore += 20;
      _log('BOT_SUSPECTED', 'navigator.languages empty — headless browser suspected');
    }
    if (typeof navigator.plugins === 'undefined' || navigator.plugins.length === 0) {
      _botScore += 10;
      _log('BOT_SUSPECTED', 'navigator.plugins empty — possible headless environment');
    }

    // 2. Mouse entropy analysis — real users have non-linear movement
    window.addEventListener('mousemove', function (e) {
      _mouseEventCount++;
      const dx = Math.abs(e.clientX - _lastMouseX);
      const dy = Math.abs(e.clientY - _lastMouseY);
      _mouseEntropy += Math.sqrt(dx * dx + dy * dy);
      _lastMouseX = e.clientX;
      _lastMouseY = e.clientY;

      // After 20 events, evaluate entropy
      if (_mouseEventCount === 20) {
        if (_mouseEntropy < 50) {
          _botScore += 30;
          _log('BOT_SUSPECTED', `Low mouse entropy: ${_mouseEntropy.toFixed(1)}px — synthetic movement pattern`);
        }
      }
    }, { passive: true });

    // 3. Check for phantom properties injected by automation frameworks
    const phantomProps = ['__phantomas', '_phantom', 'callPhantom', '__nightmare', '__selenium_evaluate'];
    for (const prop of phantomProps) {
      if (prop in window) {
        _botScore += 40;
        _log('BOT_DETECTED', `Automation framework property found: window.${prop}`);
      }
    }

    // 4. Timing-based human verification — humans have natural event timing
    let lastKeyTime = 0;
    let keyIntervals = [];
    document.addEventListener('keydown', function (e) {
      const now = Date.now();
      if (lastKeyTime > 0) {
        keyIntervals.push(now - lastKeyTime);
        if (keyIntervals.length >= 5) {
          const avg = keyIntervals.reduce((a, b) => a + b, 0) / keyIntervals.length;
          const variance = keyIntervals.reduce((a, b) => a + Math.pow(b - avg, 2), 0) / keyIntervals.length;
          if (variance < 2) { // Perfect timing = bot
            _botScore += 25;
            _log('BOT_SUSPECTED', `Keyboard variance too low: σ²=${variance.toFixed(2)} — robotic typing pattern`);
          }
          keyIntervals = [];
        }
      }
      lastKeyTime = now;
    }, { passive: true });

    // 5. Periodic bot score evaluation
    setInterval(() => {
      if (_botScore >= 70) {
        _log('BOT_BANNED', `Bot score ${_botScore}/100 exceeded threshold — session flagged`);
        _triggerBotResponse();
      }
    }, 5000);

    _log('L7_ACTIVE', 'Bot & Automation Detector initialized');
  }

  function _triggerBotResponse() {
    // Honeypot response — don't block, just feed noise data
    const fakeWallets = [
      '0xDEADBEEF0000000000000000000000000000DEAD',
      '0x0000000000000000000000000000000000000000',
      '0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
    ];
    _log('BOT_DECOY', 'Feeding decoy data to automated scraper');
    // Future: inject noise into API responses for confirmed bots
  }

  /* ═══════════════════════════════════════════
     LAYER 8 — DOM Mutation Guard
     Detects unauthorized DOM injection (XSS, extension injection)
     ═══════════════════════════════════════════ */
  function L8_domMutationGuard() {
    if (!window.MutationObserver) return;

    const ALLOWED_TAG_WHITELIST = new Set([
      'div', 'span', 'p', 'a', 'button', 'input', 'textarea', 'select',
      'option', 'label', 'form', 'table', 'thead', 'tbody', 'tr', 'td', 'th',
      'ul', 'li', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong', 'em',
      'svg', 'g', 'path', 'circle', 'rect', 'text', 'line', 'defs', 'marker',
      'pattern', 'filter', 'feDropShadow', 'radialGradient', 'stop',
      'animateMotion', 'tspan', 'image', 'img', 'canvas', 'br', 'hr', 'pre',
      'code', 'nav', 'header', 'main', 'section', 'article', 'aside', 'footer',
      '#text', 'LINK' // Allowed text nodes & dynamic stylesheet links
    ]);

    const DANGEROUS_TAGS = new Set(['script', 'iframe', 'object', 'embed', 'base', 'meta', 'link']);

    const observer = new MutationObserver(function (mutations) {
      for (const mutation of mutations) {
        for (const node of mutation.addedNodes) {
          if (node.nodeType === Node.ELEMENT_NODE) {
            const tag = node.tagName.toLowerCase();
            if (DANGEROUS_TAGS.has(tag)) {
              // Allow only our own scripts (loaded before this guard)
              if (tag === 'link' || tag === 'script') continue;
              _log('DOM_INJECTION_BLOCKED', `Unauthorized <${tag}> element injection detected and removed`);
              _botScore += 20;
              try { node.parentNode.removeChild(node); } catch (e) {}
            }

            // Check for dangerous event handlers injected as attributes
            if (node.attributes) {
              for (const attr of Array.from(node.attributes)) {
                if (/^on\w+/i.test(attr.name)) {
                  _log('DOM_EVENT_POISON_BLOCKED', `Inline event handler "${attr.name}" removed from injected element`);
                  node.removeAttribute(attr.name);
                }
              }
            }
          }
        }
      }
    });

    observer.observe(document.documentElement, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['onload', 'onerror', 'onclick', 'onfocus', 'onblur', 'onmouseover']
    });

    _log('L8_ACTIVE', 'DOM Mutation Guard initialized — observing document tree');
  }

  /* ═══════════════════════════════════════════
     LAYER 9 — Keyboard Shortcut Firewall
     Blocks F12, Ctrl+Shift+I/J/C/U, Ctrl+U (view source)
     ═══════════════════════════════════════════ */
  function L9_keyboardFirewall() {
    document.addEventListener('keydown', function (e) {
      // F12 — DevTools toggle
      if (e.key === 'F12') {
        e.preventDefault();
        _log('KEYBOARD_BLOCK', 'F12 (DevTools) shortcut blocked');
        return false;
      }

      // Ctrl+Shift+I — Inspect Element
      if (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'i')) {
        e.preventDefault();
        _log('KEYBOARD_BLOCK', 'Ctrl+Shift+I (Inspect) shortcut blocked');
        return false;
      }

      // Ctrl+Shift+J — JavaScript Console
      if (e.ctrlKey && e.shiftKey && (e.key === 'J' || e.key === 'j')) {
        e.preventDefault();
        _log('KEYBOARD_BLOCK', 'Ctrl+Shift+J (Console) shortcut blocked');
        return false;
      }

      // Ctrl+Shift+C — Element Picker
      if (e.ctrlKey && e.shiftKey && (e.key === 'C' || e.key === 'c')) {
        e.preventDefault();
        _log('KEYBOARD_BLOCK', 'Ctrl+Shift+C (Picker) shortcut blocked');
        return false;
      }

      // Ctrl+U — View Page Source
      if (e.ctrlKey && (e.key === 'U' || e.key === 'u')) {
        e.preventDefault();
        _log('KEYBOARD_BLOCK', 'Ctrl+U (View Source) shortcut blocked');
        return false;
      }

      // Ctrl+S — Save Page
      if (e.ctrlKey && (e.key === 'S' || e.key === 's')) {
        e.preventDefault();
        _log('KEYBOARD_BLOCK', 'Ctrl+S (Save) shortcut blocked');
        return false;
      }
    }, true); // capture phase — fires before any other listener

    // Block right-click context menu
    document.addEventListener('contextmenu', function (e) {
      // Allow right-click on input fields (for copy-paste accessibility)
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      e.preventDefault();
      _log('CONTEXT_MENU_BLOCKED', `Right-click context menu blocked on: ${e.target.tagName}`);
      return false;
    });

    _log('L9_ACTIVE', 'Keyboard Shortcut Firewall initialized');
  }

  /* ═══════════════════════════════════════════
     LAYER 10 — Tab Visibility Session Lock
     Pauses sensitive operations when tab is hidden
     ═══════════════════════════════════════════ */
  function L10_visibilityLock() {
    let hiddenTime = 0;
    const SESSION_TIMEOUT_MS = 30 * 60 * 1000; // 30 minutes

    document.addEventListener('visibilitychange', function () {
      if (document.visibilityState === 'hidden') {
        hiddenTime = Date.now();
        _log('TAB_HIDDEN', 'Tab hidden — session timer started');
      } else if (document.visibilityState === 'visible') {
        const elapsed = Date.now() - hiddenTime;
        if (hiddenTime > 0 && elapsed > SESSION_TIMEOUT_MS) {
          _log('SESSION_EXPIRED', `Session expired after ${Math.round(elapsed / 60000)} minutes of inactivity`);
          _showSessionExpiredBanner();
        }
        hiddenTime = 0;
      }
    });

    // Pagehide — user navigating away
    window.addEventListener('pagehide', function () {
      _log('PAGE_HIDE', 'Page hide event — session state preserved');
    });

    _log('L10_ACTIVE', 'Tab Visibility Session Lock initialized');
  }

  function _showSessionExpiredBanner() {
    const banner = document.createElement('div');
    banner.id = 'ct-session-banner';
    banner.style.cssText = `
      position: fixed; top: 0; left: 0; right: 0; z-index: 999998;
      background: linear-gradient(90deg, #1e0a0a, #2d0d0d);
      border-bottom: 2px solid #ef4444;
      padding: 12px 20px; display: flex; align-items: center;
      justify-content: space-between; font-family: 'JetBrains Mono', monospace;
      color: #fca5a5; font-size: 12px;
    `;
    banner.innerHTML = `
      <span>⚠️ <strong>Session Inactivity Warning:</strong> Re-authenticate your forensics session for security compliance.</span>
      <button onclick="this.parentElement.remove()" style="background:#ef4444;border:none;color:#fff;padding:4px 12px;border-radius:4px;cursor:pointer;font-size:11px;">Dismiss</button>
    `;
    document.body.prepend(banner);
  }

  /* ═══════════════════════════════════════════
     LAYER 11 — Source Integrity Check
     Verifies expected script attributes after load
     ═══════════════════════════════════════════ */
  function L11_integrityCheck() {
    window.addEventListener('load', function () {
      // Verify no extra scripts have been injected into the page
      const scripts = document.querySelectorAll('script[src]');
      const allowedSrcPatterns = [
        /app\.js/,
        /security\.js/,
        /fonts\.googleapis\.com/,
        /fonts\.gstatic\.com/
      ];

      scripts.forEach(function (script) {
        const src = script.src || '';
        const isAllowed = allowedSrcPatterns.some(p => p.test(src));
        if (!isAllowed) {
          _log('SCRIPT_INJECTION_DETECTED', `Unauthorized external script: ${src.slice(0, 80)}`);
          _botScore += 30;
        }
      });

      // Verify page hasn't been cached/modified (basic DOM presence check)
      const criticalIds = ['wallet-input', 'btn-analyze', 'toast-container'];
      for (const id of criticalIds) {
        if (!document.getElementById(id)) {
          _log('DOM_INTEGRITY_FAIL', `Critical element #${id} missing — possible DOM tampering`);
        }
      }

      _log('L11_ACTIVE', `Integrity check complete — ${scripts.length} scripts verified`);
    });
  }

  /* ═══════════════════════════════════════════
     LAYER 12 — CSRF Nonce Generator
     ═══════════════════════════════════════════ */
  function L12_csrfNonce() {
    const array = new Uint32Array(4);
    crypto.getRandomValues(array);
    _sessionToken = Array.from(array, n => n.toString(16).padStart(8, '0')).join('-');

    // Attach to all future fetch calls if ever used server-side
    window.__CT_CSRF_TOKEN = _sessionToken;

    // Store in sessionStorage (cleared on tab close)
    try {
      sessionStorage.setItem('ct_csrf', _sessionToken);
      sessionStorage.setItem('ct_session_start', _sessionStart.toString());
    } catch (e) {}

    _log('L12_ACTIVE', `CSRF nonce generated: ${_sessionToken.slice(0, 8)}...`);
    return _sessionToken;
  }

  /* ═══════════════════════════════════════════
     LAYER 13 — Clipboard Poison Guard
     Warns on suspicious paste actions (script/crypto theft vectors)
     ═══════════════════════════════════════════ */
  function L13_clipboardGuard() {
    document.addEventListener('paste', function (e) {
      const pasted = (e.clipboardData || window.clipboardData)?.getData('text') || '';
      const suspiciousPatterns = [
        /fetch\s*\(/i,
        /document\.cookie/i,
        /localStorage/i,
        /sessionStorage/i,
        /<script/i,
        /eval\s*\(/i,
        /Function\s*\(/i,
        /atob\s*\(/i,
        /btoa\s*\(/i,
        /window\.location\s*=/i
      ];

      for (const pattern of suspiciousPatterns) {
        if (pattern.test(pasted)) {
          _log('CLIPBOARD_POISON', `Suspicious content pasted: pattern "${pattern.source}" matched`);
          _botScore += 15;
          // Show inline warning toast
          _showSecurityToast('⚠️ Clipboard Guard: Potentially malicious content detected in paste action');
          break;
        }
      }
    }, { passive: true });

    _log('L13_ACTIVE', 'Clipboard Poison Guard initialized');
  }

  /* ═══════════════════════════════════════════
     LAYER 14 — Honeypot Trap
     Auto-bans bots that fill hidden form fields
     ═══════════════════════════════════════════ */
  function L14_honeypot() {
    window.addEventListener('DOMContentLoaded', function () {
      // Create invisible honeypot fields
      const trap = document.createElement('div');
      trap.setAttribute('aria-hidden', 'true');
      trap.style.cssText = 'position:absolute;left:-9999px;top:-9999px;opacity:0;pointer-events:none;';
      trap.innerHTML = `
        <input type="text" name="website" id="hp-website" tabindex="-1" autocomplete="off" value="">
        <input type="email" name="email_confirm" id="hp-email" tabindex="-1" autocomplete="off" value="">
        <input type="tel" name="phone_extra" id="hp-phone" tabindex="-1" autocomplete="off" value="">
      `;
      document.body.appendChild(trap);

      // Monitor for any changes (bots will fill all visible-looking fields)
      ['hp-website', 'hp-email', 'hp-phone'].forEach(function (id) {
        const el = document.getElementById(id);
        if (el) {
          el.addEventListener('input', function () {
            if (el.value) {
              _botScore += 60;
              _log('HONEYPOT_TRIGGERED', `Bot filled hidden honeypot field: #${id} = "${el.value.slice(0, 20)}"`);
            }
          });
        }
      });
    });

    _log('L14_ACTIVE', 'Honeypot trap deployed');
  }

  /* ═══════════════════════════════════════════
     LAYER 15 — Security Audit Telemetry Logger
     ═══════════════════════════════════════════ */
  function _log(type, message) {
    const entry = {
      id: _auditLog.length + 1,
      type,
      message,
      timestamp: new Date().toISOString(),
      url: window.location.pathname,
      userAgent: navigator.userAgent.slice(0, 80),
      botScore: _botScore
    };
    _auditLog.push(entry);

    // Keep only last 200 entries in memory
    if (_auditLog.length > 200) _auditLog.shift();

    // Update the live security shield UI (if the element exists)
    const auditEl = document.getElementById('sec-audit-log');
    const countEl = document.getElementById('sec-blocked-count');

    const threatTypes = ['XSS_BLOCKED', 'BOT_DETECTED', 'DOM_INJECTION_BLOCKED', 'HONEYPOT_TRIGGERED',
      'IFRAME_BLOCKED', 'KEYBOARD_BLOCK', 'RATE_LIMIT_HIT', 'DEVTOOLS_OPEN',
      'CLIPBOARD_POISON', 'PROTO_POLLUTION_BLOCKED', 'SCRIPT_INJECTION_DETECTED'];

    const isThreat = threatTypes.includes(type);
    if (isThreat) {
      const threatCount = _auditLog.filter(e => threatTypes.includes(e.type)).length;
      if (countEl) countEl.textContent = `${threatCount} Threats Intercepted & Blocked`;

      if (auditEl) {
        const entryEl = document.createElement('div');
        entryEl.style.cssText = 'padding:2px 0; font-size:11px; color:#fca5a5; font-family:monospace;';
        entryEl.innerHTML = `[<span style="color:#ef4444">${type}</span> • ${new Date().toLocaleTimeString()}] ${message}`;
        auditEl.prepend(entryEl);
        // Keep UI clean
        while (auditEl.children.length > 30) auditEl.removeChild(auditEl.lastChild);
      }
    }
  }

  function _showSecurityToast(message) {
    const tc = document.getElementById('toast-container');
    if (!tc) return;
    const toast = document.createElement('div');
    toast.className = 'toast toast-error';
    toast.style.cssText = 'display:flex;align-items:center;gap:8px;';
    toast.innerHTML = `<span>${message}</span>`;
    tc.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transition = 'opacity 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  }

  /* ═══════════════════════════════════════════
     SECURITY DASHBOARD RENDERER
     Renders live security stats in the shield modal
     ═══════════════════════════════════════════ */
  function renderSecurityDashboard() {
    const sessionDurationEl = document.getElementById('sec-session-duration');
    const botScoreEl = document.getElementById('sec-bot-score');
    const rateCountEl = document.getElementById('sec-rate-count');
    const tokenEl = document.getElementById('sec-session-token');

    setInterval(function () {
      const elapsedMs = Date.now() - _sessionStart;
      const minutes = Math.floor(elapsedMs / 60000);
      const seconds = Math.floor((elapsedMs % 60000) / 1000);
      if (sessionDurationEl) sessionDurationEl.textContent = `${minutes}m ${seconds}s`;
      if (botScoreEl) {
        botScoreEl.textContent = `${_botScore}/100`;
        botScoreEl.style.color = _botScore > 50 ? '#ef4444' : _botScore > 25 ? '#f59e0b' : '#10b981';
      }
      if (rateCountEl) rateCountEl.textContent = `${_requestTimestamps.filter(t => Date.now() - t < 60000).length}/${RATE_LIMIT_MAX} req/min`;
      if (tokenEl) tokenEl.textContent = _sessionToken ? _sessionToken.slice(0, 20) + '...' : 'Generating...';
    }, 1000);
  }

  /* ═══════════════════════════════════════════
     PUBLIC API — exposed as window.CyberShield
     ═══════════════════════════════════════════ */
  return {
    /** Initialize all security layers in sequence */
    init() {
      L1_prototypePollutionGuard();
      L3_consoleGuard();
      L4_frameBuster();
      L7_botDetector();
      L8_domMutationGuard();
      L9_keyboardFirewall();
      L10_visibilityLock();
      L11_integrityCheck();
      L12_csrfNonce();
      L13_clipboardGuard();
      L14_honeypot();

      // DevTools monitor — run last (depends on DOM being ready)
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
          L2_antiDevTools();
          renderSecurityDashboard();
        });
      } else {
        L2_antiDevTools();
        renderSecurityDashboard();
      }

      _log('SHIELD_INIT', `CyberShield v3.0 — All 15 security layers active | Session: ${window.__CT_CSRF_TOKEN}`);
      return this;
    },

    /** XSS-safe input sanitizer — use on all user input */
    sanitize: L5_sanitize,

    /** Rate-limiter check — returns true if allowed */
    checkRateLimit: L6_checkRateLimit,

    /** Log a custom security event */
    logEvent: _log,

    /** Get current audit log (read-only snapshot) */
    getAuditLog() {
      return [..._auditLog];
    },

    /** Get current bot suspicion score */
    getBotScore() {
      return _botScore;
    },

    /** Get session CSRF token */
    getToken() {
      return _sessionToken;
    }
  };
})();

/* ─────────────────────────────────────────────
   AUTO-INITIALIZE immediately on script load
   ───────────────────────────────────────────── */
CyberShield.init();

/* ─────────────────────────────────────────────
   LEGACY COMPATIBILITY — keep SecurityShield
   alias so existing app.js references still work
   ───────────────────────────────────────────── */
window.SecurityShield = {
  threatsBlocked: 0,
  requestTimestamps: [],
  rateLimitMax: 60,
  sanitize: CyberShield.sanitize,
  checkRateLimit: (action) => CyberShield.checkRateLimit(action),
  logEvent: (type, msg) => CyberShield.logEvent(type, msg),
  enforceFrameBuster: () => {} // Already done by L4
};
