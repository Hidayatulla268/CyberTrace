import re

def update_files():
    # 1. Update app.js
    with open('app.js', 'r', encoding='utf-8') as f:
        app_js = f.read()

    # Define old block to replace
    old_block = """  // Load Dossier
  function loadDossierForAddress(address) {
    const profile = generateForensicProfile(address);
    const caseId = profile.caseId || 'CYB-2026-001245';

    const caseTag = document.getElementById('dossier-modal-case-tag');
    const refId = document.getElementById('dos-ref-id');
    const targetAddr = document.getElementById('dos-target-addr');
    const riskTd = document.getElementById('dos-risk-td');
    const inflow = document.getElementById('dos-inflow');
    const outflow = document.getElementById('dos-outflow');
    const period = document.getElementById('dos-period');
    const attr = document.getElementById('dos-attr');
    const bullets = document.getElementById('dos-bullets');
    const dnaCamp = document.getElementById('dos-dna-campaign');
    const dnaMatch = document.getElementById('dos-dna-match');
    const dnaSig = document.getElementById('dos-dna-sig');

    if (caseTag) caseTag.textContent = `Case #${caseId}`;
    if (refId) refId.innerHTML = `<strong>Case Ref:</strong> ${caseId}`;
    if (targetAddr) targetAddr.textContent = address;
    if (riskTd) riskTd.innerHTML = `<span class="badge-risk badge-${profile.riskScore > 75 ? 'high' : 'medium'}">${profile.riskScore} / 100 ${profile.riskLevel}</span>`;
    if (inflow) inflow.textContent = `${profile.received} (${profile.receivedCount})`;
    if (outflow) outflow.textContent = `${profile.sent} (${profile.sentCount})`;
    if (period) period.textContent = `${profile.firstActivity} — ${profile.lastActivity}`;
    if (attr) attr.textContent = `${profile.exchange} (${profile.confidence} Conf.)`;

    if (bullets && profile.reasons) {
      bullets.innerHTML = profile.reasons.map(r => `<li>${r}</li>`).join('');
    }

    if (dnaCamp) dnaCamp.textContent = profile.matchedCampaign || 'Campaign #CYB-2048 ("Hydra-Peel" Telegram Scam)';
    if (dnaMatch) dnaMatch.textContent = `${profile.fraudDnaMatch || 91}% High Confidence`;
    if (dnaSig) {
      const camp = campaignDNAProfiles[profile.matchedCampaignId || 'CYB-2048'];
      dnaSig.textContent = camp ? camp.signatureSummary : '3-hop automated peeling chain, 80/20 tranche split, sub-minute execution, Binance off-ramp sweep.';
    }
  }

  if (btnDownloadReport && modalPdfDossier) {
    btnDownloadReport.addEventListener('click', () => {
      loadDossierForAddress(state.currentAddress);
      openModal(modalPdfDossier);
      showToast('I4C Investigation Dossier Ready for Download/Print', 'info');
    });
  }

  if (pdfPreviewTrigger && modalPdfDossier) {
    pdfPreviewTrigger.addEventListener('click', () => {
      loadDossierForAddress(state.currentAddress);
      openModal(modalPdfDossier);
    });
  }

  document.querySelectorAll('.btn-open-dossier').forEach(btn => {
    btn.addEventListener('click', () => {
      loadDossierForAddress(state.currentAddress);
      openModal(modalPdfDossier);
    });
  });

  const btnGenerateCustom = document.getElementById('btn-generate-custom-dossier');
  if (btnGenerateCustom) {
    btnGenerateCustom.addEventListener('click', () => {
      loadDossierForAddress(state.currentAddress);
      openModal(modalPdfDossier);
    });
  }

  if (btnPrintDossier) {
    btnPrintDossier.addEventListener('click', () => {
      window.print();
    });
  }"""

    new_block = """  // Load Crypto Dossier
  function loadCryptoDossier(address) {
    const profile = generateForensicProfile(address || state.currentAddress || '0xA1b2C3d4E5f6A7B8C9D0E1F2A3B4C5D6E7F8A9B0');
    const caseId = profile.caseId || 'CYB-2026-001245';

    const modalTitle = document.querySelector('#modal-pdf-dossier .modal-title-group h3');
    const caseTag = document.getElementById('dossier-modal-case-tag');
    const printArea = document.getElementById('dossier-print-area');

    if (modalTitle) modalTitle.innerHTML = 'CyberTrace &bull; I4C Crypto Forensic Dossier';
    if (caseTag) caseTag.textContent = `Case #${caseId}`;

    if (!printArea) return;

    const camp = campaignDNAProfiles[profile.matchedCampaignId || 'CYB-2048'];
    const bulletsHtml = (profile.reasons || []).map(r => `<li>${r}</li>`).join('');

    printArea.innerHTML = `
      <div class="dossier-header-banner">
        <div class="dossier-brand">
          <h2>INDIAN CYBER CRIME COORDINATION CENTRE (I4C)</h2>
          <p>Ministry of Home Affairs, Government of India &bull; Crypto Forensic Intelligence Dossier</p>
        </div>
        <div class="dossier-meta-block">
          <div><strong id="dos-ref-id">Case Ref:</strong> ${caseId}</div>
          <div><strong>Generated:</strong> ${new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })}, ${new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' })} IST</div>
          <div><strong>Classification:</strong> LAW ENFORCEMENT SENSITIVE</div>
        </div>
      </div>

      <div class="dossier-section">
        <h4>1. Executive Summary &amp; Suspect Wallet Profile</h4>
        <table class="dossier-table">
          <tr>
            <td><strong>Primary Suspect:</strong></td>
            <td class="font-mono text-cyan" id="dos-target-addr">${profile.address}</td>
            <td><strong>Assigned Threat:</strong></td>
            <td id="dos-risk-td"><span class="badge-risk badge-${profile.riskScore > 75 ? 'high' : 'medium'}">${profile.riskScore} / 100 ${profile.riskLevel}</span></td>
          </tr>
          <tr>
            <td><strong>Total Inflow:</strong></td>
            <td class="font-mono text-amber" id="dos-inflow">${profile.received} (${profile.receivedCount})</td>
            <td><strong>Total Outflow:</strong></td>
            <td class="font-mono text-muted" id="dos-outflow">${profile.sent} (${profile.sentCount})</td>
          </tr>
          <tr>
            <td><strong>Activity Period:</strong></td>
            <td id="dos-period">${profile.firstActivity} &mdash; ${profile.lastActivity}</td>
            <td><strong>Attributed Destination:</strong></td>
            <td id="dos-attr" class="text-cyan font-semibold">${profile.exchange} (${profile.confidence} Conf.)</td>
          </tr>
        </table>
      </div>

      <div class="dossier-section">
        <h4>2. Suspicious Indicators &amp; Crime Pattern</h4>
        <ul class="dossier-bullets" id="dos-bullets">
          ${bulletsHtml}
        </ul>
      </div>

      <div class="dossier-section">
        <h4>2.1 Fraud DNA™ Syndicate Fingerprint Attribution</h4>
        <table class="dossier-table">
          <tr>
            <td><strong>Matched Campaign:</strong></td>
            <td id="dos-dna-campaign" class="font-semibold text-amber">${profile.matchedCampaign || 'Campaign #CYB-2048 ("Hydra-Peel" Telegram Scam)'}</td>
            <td><strong>Fraud DNA Match:</strong></td>
            <td id="dos-dna-match" class="font-mono font-bold text-cyan">${profile.fraudDnaMatch || 91}% High Confidence</td>
          </tr>
          <tr>
            <td><strong>Behavioral Signature:</strong></td>
            <td colspan="3" id="dos-dna-sig">${camp ? camp.signatureSummary : '3-hop automated peeling chain, 80/20 tranche split, sub-minute execution, Binance off-ramp sweep.'}</td>
          </tr>
        </table>
      </div>

      <div class="dossier-section">
        <h4>3. Key Identified Addresses &amp; Recommended LEA Actions</h4>
        <table class="dossier-table">
          <thead>
            <tr>
              <th>Address</th>
              <th>Role in Flow</th>
              <th>Traced Volume</th>
              <th>Action Recommended</th>
            </tr>
          </thead>
          <tbody id="dos-roles-tbody">
            <tr>
              <td class="font-mono text-cyan">${profile.shortAddress}</td>
              <td>Suspect Collection Hub</td>
              <td class="font-mono font-bold">${profile.received}</td>
              <td>Emergency Freeze Request</td>
            </tr>
            <tr>
              <td class="font-mono">${profile.muleA}</td>
              <td>Layer-1 Intermediary Splitter</td>
              <td class="font-mono">${profile.flowAmounts ? profile.flowAmounts.split1 : '₹50,700'}</td>
              <td>Subpoena Cluster Records</td>
            </tr>
            <tr>
              <td class="font-mono">${profile.muleB}</td>
              <td>Layer-2 Layering Mule</td>
              <td class="font-mono">${profile.flowAmounts ? profile.flowAmounts.split2 : '₹33,800'}</td>
              <td>Subpoena Secondary Records</td>
            </tr>
            <tr>
              <td class="font-mono text-cyan">${profile.exchange.split(' ')[0]} Gateway</td>
              <td>${profile.exchange}</td>
              <td class="font-mono text-cyan">${profile.flowAmounts ? profile.flowAmounts.cexSweep : '₹84,500'}</td>
              <td>Section 91 CrPC / Section 94 BNSS Subpoena &amp; KYC Freeze</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="dossier-footer">
        <div class="dossier-stamp">VERIFIED BY CYBERTRACE AUTOMATED ENGINE (PS-26183) &bull; SHA256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</div>
      </div>
    `;
  }

  // Load UPI & Banking Dossier
  function loadBankingDossier(upiOrUtr) {
    const p = generateBankingProfile(upiOrUtr || state.currentUpi || (upiInput ? upiInput.value : 'daily.payout@oksbi'));
    const modalTitle = document.querySelector('#modal-pdf-dossier .modal-title-group h3');
    const caseTag = document.getElementById('dossier-modal-case-tag');
    const printArea = document.getElementById('dossier-print-area');

    if (modalTitle) modalTitle.innerHTML = 'CyberTrace &bull; I4C UPI &amp; Core Banking Forensic Dossier';
    if (caseTag) caseTag.textContent = `NCRP #${p.complaintsCount}812-2026`;

    if (!printArea) return;

    printArea.innerHTML = `
      <div class="dossier-header-banner">
        <div class="dossier-brand">
          <h2>INDIAN CYBER CRIME COORDINATION CENTRE (I4C)</h2>
          <p>Ministry of Home Affairs, Government of India &bull; UPI &amp; Core Banking Forensic Intelligence Dossier</p>
        </div>
        <div class="dossier-meta-block">
          <div><strong id="dos-ref-id">Case Ref:</strong> NCRP-1930-${p.complaintsCount}812-2026</div>
          <div><strong>Generated:</strong> ${new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })}, ${new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' })} IST</div>
          <div><strong>Classification:</strong> LAW ENFORCEMENT SENSITIVE &bull; SECTION 65B EVIDENCE READY</div>
        </div>
      </div>

      <div class="dossier-section">
        <h4>1. Executive Summary &amp; Suspect Beneficiary Banking Profile</h4>
        <table class="dossier-table">
          <tr>
            <td><strong>Suspect Identifier:</strong></td>
            <td class="font-mono text-cyan"><strong>${p.input}</strong></td>
            <td><strong>Beneficiary Entity:</strong></td>
            <td class="font-mono"><strong>${p.alias}</strong></td>
          </tr>
          <tr>
            <td><strong>Linked Bank &amp; Branch:</strong></td>
            <td>${p.bankName}, ${p.branch}</td>
            <td><strong>IFSC Code:</strong></td>
            <td class="font-mono text-cyan">${p.ifsc}</td>
          </tr>
          <tr>
            <td><strong>Full Account Number:</strong></td>
            <td class="font-mono"><strong>${p.accFull}</strong> (Masked: ${p.accMasked})</td>
            <td><strong>Account Status:</strong></td>
            <td><span class="badge-risk badge-high">⚠️ Flagged Mule Account</span></td>
          </tr>
          <tr>
            <td><strong>Total Inflow Volume:</strong></td>
            <td class="font-mono font-bold text-amber">${p.totalInflow} (${p.txCount})</td>
            <td><strong>Actionable Retrievable Balance:</strong></td>
            <td class="font-mono font-bold text-green">${p.retrievable} (Active)</td>
          </tr>
          <tr>
            <td><strong>Device &amp; SIM Telemetry:</strong></td>
            <td colspan="3">${p.simStatus} &bull; ${p.ipLocation}</td>
          </tr>
        </table>
      </div>

      <div class="dossier-section">
        <h4>2. National Cyber Crime Reporting Portal (NCRP 1930) Correlation</h4>
        <table class="dossier-table">
          <tr>
            <td><strong>Linked Police FIRs / NCRP:</strong></td>
            <td class="font-bold text-red">${p.complaintsCount} Active Complaints on 1930 Portal</td>
            <td><strong>Total Syndicate Loss:</strong></td>
            <td class="font-mono font-bold text-amber">${p.totalLoss}</td>
          </tr>
          <tr>
            <td><strong>Modus Operandi:</strong></td>
            <td colspan="3" class="text-cyan font-bold">${p.moType}</td>
          </tr>
        </table>
        <ul class="dossier-bullets mt-2">
          <li>Immediate automated layering from victim account into multi-tier mule network within 15 minutes.</li>
          <li>Coordinated ATM cash-out sweeps detected (${p.atmCash} withdrawn at ATM SBI-Surat-0442).</li>
          <li>Remaining retrievable funds of <strong>${p.retrievable}</strong> currently available in Layer 2 Account (${p.mule1Acc}) ready for immediate debit-freeze.</li>
        </ul>
      </div>

      <div class="dossier-section">
        <h4>3. Multi-Tier Banking Layering &amp; Mule Routing Breakdown</h4>
        <table class="dossier-table">
          <thead>
            <tr>
              <th>Hop Level</th>
              <th>Account / Identifier</th>
              <th>Bank &amp; Branch</th>
              <th>Traced Amount</th>
              <th>Status / LEA Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Tier 1 (Origin)</strong></td>
              <td class="font-mono text-cyan">${p.input}</td>
              <td>${p.bankName}</td>
              <td class="font-mono font-bold">${p.totalInflow}</td>
              <td>Victim Debit Inflow</td>
            </tr>
            <tr>
              <td><strong>Tier 2 (Mule A - 60%)</strong></td>
              <td class="font-mono">${p.mule1Acc}</td>
              <td>${p.mule1Bank}</td>
              <td class="font-mono text-amber">${p.split1}</td>
              <td><strong class="text-green">${p.retrievable} Available</strong> (Lien-Mark / Freeze)</td>
            </tr>
            <tr>
              <td><strong>Tier 2 (Mule B - 40%)</strong></td>
              <td class="font-mono">${p.mule2Acc}</td>
              <td>${p.mule2Bank}</td>
              <td class="font-mono text-amber">${p.split2}</td>
              <td>Secondary Layering Subpoena</td>
            </tr>
            <tr>
              <td><strong>Tier 3 (Cash-Out)</strong></td>
              <td class="font-mono">ATM Surat-0442</td>
              <td>State Bank of India</td>
              <td class="font-mono text-red">${p.atmCash}</td>
              <td>CCTV Footage &amp; GPS Requisition</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="dossier-section">
        <h4>4. Statutory Order under Section 91 CrPC, 1973 &amp; Section 94 BNSS, 2023</h4>
        <div style="background: rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 12px; font-family: var(--font-mono); font-size: 0.76rem; line-height: 1.5; white-space: pre-wrap; color: #e2e8f0;">
TO: The Nodal Officer / Law Enforcement Liaison Cell, ${p.bankName}, ${p.branch}
SUBJECT: MANDATORY REQUISITION TO IMMEDIATELY FREEZE / DEBIT-BLOCK MULE ACCOUNT (${p.accFull}) IN NCRP CASE #${p.complaintsCount}812

You are hereby commanded under Section 91 of Code of Criminal Procedure, 1973 / Section 94 of Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023 to immediately:
1. Place a TOTAL DEBIT FREEZE on Account ${p.accFull} (Holder: ${p.alias}, IFSC: ${p.ifsc}) and lien-mark ${p.retrievable}.
2. Preserve all KYC documents, Account Opening Form (AOF), linked mobile numbers, and ATM CCTV footage.
3. Furnish compliance report within 24 hours to the Investigating Officer, Cyber Crime Police Station / I4C CIS Division.
        </div>
      </div>

      <div class="dossier-footer">
        <div class="dossier-stamp">VERIFIED BY CYBERTRACE BANKING &amp; UPI FORENSIC ENGINE (I4C / NPCI CBS) &bull; SHA256:f812a4b9c1d0e4f6a8b2c0d4e6f8a0b2c4d6e8f0a2c4e6f8a0b2c4d6e8f0a2c4</div>
      </div>
    `;
  }

  // Universal Dossier Dispatcher (Crypto & UPI)
  function loadDossier(target) {
    const isBankingTarget = (typeof target === 'string' && (target.includes('@') || target.startsWith('UTR') || /^\\d{10}$/.test(target) || target.includes('BANK') || target.includes('NCRP')));
    const isBankingMode = state.currentEngineMode === 'banking';
    
    if (isBankingTarget || (isBankingMode && (!target || !target.startsWith('0x')))) {
      const upi = isBankingTarget ? target : (state.currentUpi || (upiInput ? upiInput.value : 'daily.payout@oksbi'));
      loadBankingDossier(upi);
    } else {
      const addr = (typeof target === 'string' && target.startsWith('0x')) ? target : (state.currentAddress || (walletInput ? walletInput.value : '0xA1b2C3d4E5f6A7B8C9D0E1F2A3B4C5D6E7F8A9B0'));
      loadCryptoDossier(addr);
    }
  }

  // Backward-compatible alias
  function loadDossierForAddress(address) {
    loadDossier(address);
  }

  if (btnDownloadReport && modalPdfDossier) {
    btnDownloadReport.addEventListener('click', () => {
      loadDossier(state.currentEngineMode === 'banking' ? state.currentUpi : state.currentAddress);
      openModal(modalPdfDossier);
      showToast('I4C Investigation Dossier Ready for Download/Print', 'info');
    });
  }

  if (pdfPreviewTrigger && modalPdfDossier) {
    pdfPreviewTrigger.addEventListener('click', () => {
      loadDossier(state.currentEngineMode === 'banking' ? state.currentUpi : state.currentAddress);
      openModal(modalPdfDossier);
    });
  }

  document.querySelectorAll('.btn-open-dossier').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.upi || btn.dataset.address || btn.dataset.case || (state.currentEngineMode === 'banking' ? (state.currentUpi || (upiInput ? upiInput.value : 'daily.payout@oksbi')) : state.currentAddress);
      loadDossier(target);
      openModal(modalPdfDossier);
      showToast('I4C Investigation Dossier Ready for Download/Print', 'info');
    });
  });

  const btnGenerateCustom = document.getElementById('btn-generate-custom-dossier');
  if (btnGenerateCustom) {
    btnGenerateCustom.addEventListener('click', () => {
      loadDossier(state.currentEngineMode === 'banking' ? state.currentUpi : state.currentAddress);
      openModal(modalPdfDossier);
      showToast('Generated Active Investigation Dossier for Print / Download', 'success');
    });
  }

  if (btnPrintDossier) {
    btnPrintDossier.addEventListener('click', () => {
      window.print();
    });
  }"""

    if old_block in app_js:
        app_js = app_js.replace(old_block, new_block)
        print("Replaced dossier block in app.js successfully!")
    else:
        print("Warning: exact old_block not found in app.js, checking regex replacement...")
        # fallback regex replace
        pattern = r"  // Load Dossier\s+function loadDossierForAddress\(address\) \{[\s\S]*?if \(btnPrintDossier\) \{\s+btnPrintDossier\.addEventListener\('click', \(\) => \{\s+window\.print\(\);\s+\}\);\s+\}"
        app_js = re.sub(pattern, new_block, app_js)
        print("Regex replaced dossier block in app.js!")

    # Update btnPrintBankingFreeze in app.js
    old_freeze_print = """  if (btnPrintBankingFreeze) {
    btnPrintBankingFreeze.addEventListener('click', () => {
      window.print();
    });
  }"""

    new_freeze_print = """  if (btnPrintBankingFreeze) {
    btnPrintBankingFreeze.addEventListener('click', () => {
      const val = (upiInput ? upiInput.value.trim() : '') || state.currentUpi || 'daily.payout@oksbi';
      loadBankingDossier(val);
      openModal(modalPdfDossier);
      showToast('I4C Section 91 Bank Freeze Dossier & Print Preview Ready', 'success');
    });
  }"""

    app_js = app_js.replace(old_freeze_print, new_freeze_print)

    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(app_js)

    # 2. Update index.html view-reports table
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    old_table_body = """                <tbody>
                  <tr>
                    <td><span class="font-mono text-cyan font-bold">CYB-2026-001245</span></td>
                    <td class="font-mono">0xA1b2...A9B0</td>
                    <td>Task-Based Fraud</td>
                    <td><span class="badge-risk badge-high">87 HIGH</span></td>
                    <td class="font-mono font-semibold">₹8,42,000</td>
                    <td>Binance (Cluster) &bull; 91%</td>
                    <td><button class="btn-ghost-sm btn-open-dossier" data-case="CYB-2026-001245">Download Dossier PDF</button></td>
                  </tr>
                  <tr>
                    <td><span class="font-mono text-cyan font-bold">CYB-2026-009812</span></td>
                    <td class="font-mono">0x742d...f44e</td>
                    <td>Ransomware Extortion</td>
                    <td><span class="badge-risk badge-high">98 CRITICAL</span></td>
                    <td class="font-mono font-semibold">₹34,50,000</td>
                    <td>Tornado Cash Mixer &bull; 99%</td>
                    <td><button class="btn-ghost-sm btn-open-dossier" data-case="CYB-2026-009812">Download Dossier PDF</button></td>
                  </tr>
                  <tr>
                    <td><span class="font-mono text-cyan font-bold">CYB-2026-003410</span></td>
                    <td class="font-mono">0x8920...43e7</td>
                    <td>Investment Scam</td>
                    <td><span class="badge-risk badge-high">74 HIGH</span></td>
                    <td class="font-mono font-semibold">₹4,15,000</td>
                    <td>KuCoin Gateway &bull; 84%</td>
                    <td><button class="btn-ghost-sm btn-open-dossier" data-case="CYB-2026-003410">Download Dossier PDF</button></td>
                  </tr>
                </tbody>"""

    new_table_body = """                <tbody>
                  <!-- CRYPTO ENGINE CASES -->
                  <tr>
                    <td><span class="font-mono text-cyan font-bold">CYB-2026-001245</span></td>
                    <td class="font-mono">0xA1b2...A9B0</td>
                    <td>Task-Based Crypto Fraud</td>
                    <td><span class="badge-risk badge-high">87 HIGH</span></td>
                    <td class="font-mono font-semibold">₹8,42,000</td>
                    <td>Binance (Cluster) &bull; 91%</td>
                    <td><button class="btn-ghost-sm btn-open-dossier" data-case="CYB-2026-001245" data-address="0xA1b2C3d4E5f6A7B8C9D0E1F2A3B4C5D6E7F8A9B0">Download Dossier PDF</button></td>
                  </tr>
                  <tr>
                    <td><span class="font-mono text-cyan font-bold">CYB-2026-009812</span></td>
                    <td class="font-mono">0x742d...f44e</td>
                    <td>Ransomware Extortion</td>
                    <td><span class="badge-risk badge-high">98 CRITICAL</span></td>
                    <td class="font-mono font-semibold">₹34,50,000</td>
                    <td>Tornado Cash Mixer &bull; 99%</td>
                    <td><button class="btn-ghost-sm btn-open-dossier" data-case="CYB-2026-009812" data-address="0x742d35Cc6634C0532925a3b844Bc454e4438f44e">Download Dossier PDF</button></td>
                  </tr>
                  <tr>
                    <td><span class="font-mono text-cyan font-bold">CYB-2026-003410</span></td>
                    <td class="font-mono">0x8920...43e7</td>
                    <td>Pig Butchering Investment</td>
                    <td><span class="badge-risk badge-high">74 HIGH</span></td>
                    <td class="font-mono font-semibold">₹4,15,000</td>
                    <td>KuCoin Gateway &bull; 84%</td>
                    <td><button class="btn-ghost-sm btn-open-dossier" data-case="CYB-2026-003410" data-address="0x89205A3E3b2A69De6DBf7F01ed13B2108B2C43e7">Download Dossier PDF</button></td>
                  </tr>
                  <!-- UPI & BANKING RAILS CASES -->
                  <tr>
                    <td><span class="font-mono text-green font-bold">NCRP-1930-1481</span></td>
                    <td class="font-mono text-green">daily.payout@oksbi</td>
                    <td>Telegram Job Scam (UPI)</td>
                    <td><span class="badge-risk badge-high">94 HIGH</span></td>
                    <td class="font-mono font-semibold">₹84,500</td>
                    <td>State Bank of India (Surat Mule)</td>
                    <td><button class="btn-ghost-sm btn-open-dossier" data-upi="daily.payout@oksbi">Download Dossier PDF</button></td>
                  </tr>
                  <tr>
                    <td><span class="font-mono text-green font-bold">NCRP-1930-2284</span></td>
                    <td class="font-mono text-green">cbi.investigation.fund@okaxis</td>
                    <td>Digital Arrest Extortion (UPI)</td>
                    <td><span class="badge-risk badge-high">96 CRITICAL</span></td>
                    <td class="font-mono font-semibold">₹1,50,000</td>
                    <td>Axis Bank (Delhi Escrow)</td>
                    <td><button class="btn-ghost-sm btn-open-dossier" data-upi="cbi.investigation.fund@okaxis">Download Dossier PDF</button></td>
                  </tr>
                  <tr>
                    <td><span class="font-mono text-green font-bold">NCRP-1930-0641</span></td>
                    <td class="font-mono text-green">UTR-20260825-991240</td>
                    <td>Fake Electricity APK Scam (UTR)</td>
                    <td><span class="badge-risk badge-high">88 HIGH</span></td>
                    <td class="font-mono font-semibold">₹42,000</td>
                    <td>Punjab National Bank (Chandigarh)</td>
                    <td><button class="btn-ghost-sm btn-open-dossier" data-upi="UTR-20260825-991240">Download Dossier PDF</button></td>
                  </tr>
                </tbody>"""

    html = html.replace(old_table_body, new_table_body)

    # Also update table header to indicate Wallet / VPA / UTR and CEX / Beneficiary Bank
    html = html.replace(
        "<th>Target Suspect Wallet</th>",
        "<th>Target Identifier (Wallet / VPA / UTR)</th>"
    )
    html = html.replace(
        "<th>Attributed Exchange</th>",
        "<th>Attributed CEX / Beneficiary Bank</th>"
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html successfully!")

    # 3. Update style.css for print support
    with open('style.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # Ensure printable dossier styles include crisp backgrounds, high contrast text and proper table rendering in print
    old_print_css = """/* PRINT STYLES */
@media print {
  body * {
    visibility: hidden;
  }
  .printable-dossier, .printable-dossier * {
    visibility: visible;
  }
  .printable-dossier {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    background: #ffffff !important;
    color: #000000 !important;
  }
  .no-print {
    display: none !important;
  }
  .dossier-sheet {
    background: #ffffff !important;
    color: #000000 !important;
    border: none !important;
  }
}"""

    new_print_css = """/* PRINT STYLES */
@media print {
  body * {
    visibility: hidden;
  }
  .printable-dossier, .printable-dossier * {
    visibility: visible;
  }
  .printable-dossier {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    background: #ffffff !important;
    color: #0f172a !important;
  }
  .no-print {
    display: none !important;
  }
  .dossier-sheet {
    background: #ffffff !important;
    color: #0f172a !important;
    border: none !important;
    padding: 0 !important;
  }
  .dossier-brand h2 {
    color: #0f172a !important;
  }
  .dossier-brand p {
    color: #475569 !important;
  }
  .dossier-section h4 {
    color: #0369a1 !important;
  }
  .dossier-table {
    border-color: #cbd5e1 !important;
  }
  .dossier-table td, .dossier-table th {
    border-color: #cbd5e1 !important;
    color: #0f172a !important;
  }
  .dossier-table th {
    background: #f1f5f9 !important;
  }
  .dossier-bullets {
    color: #334155 !important;
  }
  .dossier-stamp {
    color: #64748b !important;
  }
}"""

    css = css.replace(old_print_css, new_print_css)

    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated style.css successfully!")

if __name__ == '__main__':
    update_files()
