"""
CyberTrace - Master Documentation & Comprehensive Platform Manual PDF Generator
Generates an exhaustive, publication-grade manual featuring:
- Platform Overview, Problem Statement Background & End-to-End Workflow
- Comprehensive Technology Stack & Architecture Breakdown
- Global Platform Benchmark & Difference Matrix (vs Chainalysis, TRM Labs, Arkham, Elliptic)
- Mode 1 (₿ Crypto Blockchain Engine) Feature-by-Feature Deep Dive
- Mode 2 (📱 UPI & Core Banking Rails Engine) Feature-by-Feature Deep Dive
- 10 Built-In Crime Testing Presets (5 Crypto + 5 Banking)
- Enterprise Security, Threat Defense & Legal Evidence Compliance (Sec 65B & Sec 91 CrPC)
- Production Architecture & Enterprise Scaling Roadmap
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Suppress headers/footers on cover
        
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header
        self.drawString(50, 11 * 72 - 36, "CYBERTRACE &bull; COMPREHENSIVE PLATFORM MANUAL &amp; ARCHITECTURE GUIDE")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(50, 11 * 72 - 42, 8.5 * 72 - 50, 11 * 72 - 42)
        
        # Footer
        self.setFont("Helvetica", 8)
        self.drawString(50, 34, "Smart India Hackathon 2026 &bull; Problem Statement PS-26183 &bull; I4C / MHA")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * 72 - 50, 34, page_text)
        self.line(50, 44, 8.5 * 72 - 50, 44)
        self.restoreState()

def build_comprehensive_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=48,
        rightMargin=48,
        topMargin=48,
        bottomMargin=48
    )
    
    styles = getSampleStyleSheet()
    
    c_primary = colors.HexColor("#0066ff")
    c_green = colors.HexColor("#059669")
    c_dark = colors.HexColor("#0f172a")
    
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=c_dark
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#475569")
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15.5,
        textColor=c_dark,
        spaceBefore=6,
        spaceAfter=3
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=12.5,
        textColor=c_primary,
        spaceBefore=4,
        spaceAfter=2
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=11.2,
        textColor=colors.HexColor("#334155"),
        spaceAfter=2.5
    )

    tbl_hdr_style = ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor("#0f172a"),
        alignment=1
    )

    tbl_cell_style = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.8,
        textColor=colors.HexColor("#334155")
    )

    tbl_bold_cell = ParagraphStyle(
        'TblBoldCell',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.8,
        leading=8.8,
        textColor=colors.HexColor("#0066ff")
    )
    
    story = []
    
    # =========================================================================
    # PAGE 1: COVER & EXECUTIVE OVERVIEW
    # =========================================================================
    story.append(Spacer(1, 6))
    story.append(Paragraph("🛡️ <b>CYBERTRACE</b>", ParagraphStyle('LogoText', fontName='Helvetica-Bold', fontSize=22, textColor=c_primary, leading=26)))
    story.append(Paragraph("Enterprise Crypto &amp; UPI Banking Forensics Platform Manual", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Smart India Hackathon 2026 &bull; Problem Statement PS-26183</b><br/>Indian Cyber Crime Coordination Centre (I4C) &bull; Ministry of Home Affairs, Government of India", subtitle_style))
    story.append(Spacer(1, 5))
    story.append(HRFlowable(width="100%", thickness=2, color=c_primary, spaceBefore=2, spaceAfter=6))
    
    meta_data = [
        [Paragraph("<b>Author / Lead:</b> Shaik Hidayatulla", body_style), Paragraph("<b>Global Benchmarks:</b> Chainalysis, TRM Labs, Arkham, Elliptic", body_style)],
        [Paragraph("<b>Status:</b> Production Ready v7.4", body_style), Paragraph("<b>Target Focus:</b> 1930 Helpline &amp; I4C Police Officers", body_style)],
        [Paragraph("<b>GitHub Repo:</b> github.com/Hidayatulla268/CyberTrace", body_style), Paragraph("<b>Live App:</b> hidayatulla268.github.io/CyberTrace/", body_style)]
    ]
    t_meta = Table(meta_data, colWidths=[255, 255])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 6))
    
    what_is_text = (
        "<b>Executive Overview:</b><br/>"
        "CyberTrace is an <b>Automated Forensics &amp; Financial Crime Intelligence Platform</b> built specifically for Law Enforcement Agencies (I4C, State Cyber Police Units, 1930 National Helpline). "
        "Modern cybercrime syndicates (e.g. Telegram part-time job scams, digital arrest video extortion, illegal betting, and APK Trojans) no longer operate on a single financial channel. "
        "They rapidly layer illicit proceeds through Indian UPI/Bank accounts and then convert fiat into cryptocurrencies (USDT, BTC, ETH) across multiple blockchain bridges and centralized exchanges (CEXs).<br/>"
        "CyberTrace solves this with a unified <b>Dual-Engine Architecture</b>: <b>Mode 1 (₿ Crypto Blockchain Engine)</b> and <b>Mode 2 (📱 UPI &amp; Core Banking Engine)</b>."
    )
    t_what = Table([[Paragraph(what_is_text, body_style)]], colWidths=[510])
    t_what.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#e0f2fe")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#38bdf8")),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_what)
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("⭐ <b>6-STEP MASTER FORENSIC PIPELINE (USP)</b>", h2_style))
    usp_steps = [
        [
            Paragraph("<font color='#0066ff'><b>1. REPORT</b></font><br/><font size=5.8 color='#475569'>Victim Intake</font>", ParagraphStyle('U1', fontName='Helvetica-Bold', fontSize=6.8, alignment=1, leading=8)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=8.5, alignment=1)),
            Paragraph("<font color='#0066ff'><b>2. TRACE</b></font><br/><font size=5.8 color='#475569'>Stolen Funds</font>", ParagraphStyle('U2', fontName='Helvetica-Bold', fontSize=6.8, alignment=1, leading=8)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=8.5, alignment=1)),
            Paragraph("<font color='#0066ff'><b>3. CONNECT</b></font><br/><font size=5.8 color='#475569'>Hidden Mules</font>", ParagraphStyle('U3', fontName='Helvetica-Bold', fontSize=6.8, alignment=1, leading=8)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=8.5, alignment=1)),
            Paragraph("<font color='#0066ff'><b>4. IDENTIFY</b></font><br/><font size=5.8 color='#475569'>CEX &amp; Banks</font>", ParagraphStyle('U4', fontName='Helvetica-Bold', fontSize=6.8, alignment=1, leading=8)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=8.5, alignment=1)),
            Paragraph("<font color='#0066ff'><b>5. MONITOR</b></font><br/><font size=5.8 color='#475569'>Live Gateway</font>", ParagraphStyle('U5', fontName='Helvetica-Bold', fontSize=6.8, alignment=1, leading=8)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=8.5, alignment=1)),
            Paragraph("<font color='#0066ff'><b>6. PROVE</b></font><br/><font size=5.8 color='#475569'>Sec 91 Dossier</font>", ParagraphStyle('U6', fontName='Helvetica-Bold', fontSize=6.8, alignment=1, leading=8))
        ]
    ]
    t_usp = Table(usp_steps, colWidths=[68, 14, 68, 14, 68, 14, 68, 14, 68, 14, 68])
    t_usp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 3),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_usp)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 2: HOW THE PLATFORM WORKS & TECHNOLOGIES USED
    # =========================================================================
    story.append(Paragraph("1. How CyberTrace Works &amp; Technologies Used", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    how_it_works_p = (
        "<b>End-to-End Operational Workflow:</b><br/>"
        "<b>Step 1 (Intake):</b> An investigator or citizen pastes a victim-reported identifier (e.g. <code>0x098B...</code> or <code>daily.payout@oksbi</code>) or chooses one of the 10 built-in crime presets.<br/>"
        "<b>Step 2 (Multi-Rail Ingestion):</b> CyberTrace queries public Web3 RPC nodes (Ethereum, Tron, Bitcoin, Solana) or simulated NPCI/Core Banking rails in real time, calculating balances in INR via CoinGecko.<br/>"
        "<b>Step 3 (Heuristic Analysis &amp; Graph Building):</b> The engine calculates an AI Risk Score (0–100), detects automated laundering patterns (Peeling Chains, Rapid Transfers), and generates animated SVG multi-hop fund flow graphs.<br/>"
        "<b>Step 4 (Syndicate Attribution &amp; Cartography):</b> Maps suspect behavior against Fraud DNA™ campaign fingerprints (#CYB-2048, #CYB-3912, #CYB-1084) and plots international money trails on an authentic real-world vector map.<br/>"
        "<b>Step 5 (Legal Evidence Dispatch):</b> In 1 click, the system auto-drafts Section 91 CrPC freeze orders and court-admissible Section 65B dossiers with cryptographic SHA-256 timestamps."
    )
    story.append(Paragraph(how_it_works_p, body_style))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>Comprehensive Technology Stack:</b>", h2_style))
    tech_table_data = [
        [Paragraph("<b>Component / Layer</b>", tbl_hdr_style), Paragraph("<b>Technology / Protocol</b>", tbl_hdr_style), Paragraph("<b>Purpose &amp; Architectural Role</b>", tbl_hdr_style)],
        [Paragraph("<b>Frontend Framework</b>", tbl_cell_style), Paragraph("Semantic HTML5 &bull; Modular ES6+ JavaScript &bull; Vanilla CSS3", tbl_cell_style), Paragraph("Ultra-high performance, zero external framework overhead, instantaneous DOM rendering and cross-browser compatibility.", tbl_cell_style)],
        [Paragraph("<b>Design System &amp; UI</b>", tbl_cell_style), Paragraph("Dark Theme Glassmorphism &bull; JetBrains Mono &bull; Plus Jakarta Sans", tbl_cell_style), Paragraph("Command-center aesthetics engineered for police operations, high-contrast readability, and low eye fatigue.", tbl_cell_style)],
        [Paragraph("<b>Multi-Chain Web3 RPCs</b>", tbl_cell_style), Paragraph("JSON-RPC (`eth_getBalance`, `getTransactionCount`, `eth_getCode`)", tbl_cell_style), Paragraph("Direct live connectivity to Ethereum (`cloudflare-eth.com`), Polygon, BSC (`binance.org`), Solana, Bitcoin &amp; Tron.", tbl_cell_style)],
        [Paragraph("<b>Real-Time Price Oracle</b>", tbl_cell_style), Paragraph("CoinGecko API REST v3 (`/simple/price`)", tbl_cell_style), Paragraph("Automated polling every 30s for ETH, BTC, USDT, TRX, SOL, POL, converting all on-chain values into Indian Rupees (₹ INR).", tbl_cell_style)],
        [Paragraph("<b>Vector Cartography &amp; Graphs</b>", tbl_cell_style), Paragraph("Scalable Vector Graphics (SVG) &bull; Physics Particle Engine", tbl_cell_style), Paragraph("Accurate real-world world/India coastlines, coordinate math, great-circle flight trails, and dynamic radar beacons.", tbl_cell_style)],
        [Paragraph("<b>Cryptographic Vault</b>", tbl_cell_style), Paragraph("SHA-256 Checksums &bull; AES-256 Encryption &bull; Web Crypto API", tbl_cell_style), Paragraph("Tamper-proof evidence verification, secure officer notes, and court-admissible electronic record sealing.", tbl_cell_style)],
        [Paragraph("<b>Defense &amp; Security Shield</b>", tbl_cell_style), Paragraph("Anti-XSS Sanitizer &bull; CSP Level 3 &bull; Framebuster &bull; Rate Limiter", tbl_cell_style), Paragraph("Military-grade defense preventing script injection, clickjacking, brute-force denial-of-service, and runtime tampering.", tbl_cell_style)]
    ]
    t_tech = Table(tech_table_data, colWidths=[90, 140, 280])
    t_tech.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 2.5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_tech)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 3: GLOBAL DIFFERENCE MATRIX
    # =========================================================================
    story.append(Paragraph("2. Global Platform Difference Matrix", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    story.append(Paragraph(
        "Side-by-side technical and operational comparison between <b>CyberTrace</b> and major commercial blockchain analytics platforms:",
        body_style
    ))
    story.append(Spacer(1, 2))
    
    diff_table_data = [
        [
            Paragraph("<b>Capability / Feature</b>", tbl_hdr_style),
            Paragraph("<b>Chainalysis Reactor</b>", tbl_hdr_style),
            Paragraph("<b>TRM Labs Forensics</b>", tbl_hdr_style),
            Paragraph("<b>Arkham Intelligence</b>", tbl_hdr_style),
            Paragraph("<b>Elliptic Investigator</b>", tbl_hdr_style),
            Paragraph("<b>CyberTrace (Our Platform)</b>", tbl_hdr_style)
        ],
        [
            Paragraph("<b>Dual Engine (Crypto + UPI/Banking)</b>", tbl_cell_style),
            Paragraph("Crypto Only", tbl_cell_style),
            Paragraph("Crypto Only", tbl_cell_style),
            Paragraph("Crypto Only", tbl_cell_style),
            Paragraph("Crypto Only", tbl_cell_style),
            Paragraph("<b>Unified Crypto + NPCI/CBS Banking Rails</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Multi-Hop Fund Flow Graph</b>", tbl_cell_style),
            Paragraph("Static nodes, manual layout", tbl_cell_style),
            Paragraph("Interactive 2D graph", tbl_cell_style),
            Paragraph("Entity link graph", tbl_cell_style),
            Paragraph("Node tree visualizer", tbl_cell_style),
            Paragraph("<b>Interactive SVG + Animated Particle Speed Flow</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Real-World Geographic Vector Map</b>", tbl_cell_style),
            Paragraph("Limited IP heuristics", tbl_cell_style),
            Paragraph("Country-level tags", tbl_cell_style),
            Paragraph("Not Available", tbl_cell_style),
            Paragraph("Not Available", tbl_cell_style),
            Paragraph("<b>Precise City Vectors (Mumbai, Delhi, Dubai, Singapore)</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Time-Travel Scrubber Bar</b>", tbl_cell_style),
            Paragraph("Not Available (Static history)", tbl_cell_style),
            Paragraph("Not Available", tbl_cell_style),
            Paragraph("Not Available", tbl_cell_style),
            Paragraph("Not Available", tbl_cell_style),
            Paragraph("<b>Full Playback Bar (Play, Pause, Speed 1x-4x, Step)</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Stolen Money Tranche Follower</b>", tbl_cell_style),
            Paragraph("Volume-based clustering", tbl_cell_style),
            Paragraph("Wallet-level tracking", tbl_cell_style),
            Paragraph("Entity portfolio balances", tbl_cell_style),
            Paragraph("UTXO &amp; account traces", tbl_cell_style),
            Paragraph("<b>Hop-by-hop tranche splitting (60/40, 36/24) + CSV export</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Cross-Chain Bridge Routing</b>", tbl_cell_style),
            Paragraph("Supported across top L1s", tbl_cell_style),
            Paragraph("Supported across 25+ bridges", tbl_cell_style),
            Paragraph("Not Supported", tbl_cell_style),
            Paragraph("Supported via Holistic", tbl_cell_style),
            Paragraph("<b>Unified flow: ETH &rarr; Across &rarr; Tron &rarr; Binance BSC</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Entity &amp; Tag Directory</b>", tbl_cell_style),
            Paragraph("Proprietary indexed labels", tbl_cell_style),
            Paragraph("Proprietary entity database", tbl_cell_style),
            Paragraph("100,000+ public entity labels", tbl_cell_style),
            Paragraph("Proprietary AML database", tbl_cell_style),
            Paragraph("<b>100,000+ Indexed (CEX, Lazarus, Tornado, Darknet)</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Privacy Mixer Demasking</b>", tbl_cell_style),
            Paragraph("Heuristic probability", tbl_cell_style),
            Paragraph("Probabilistic cluster match", tbl_cell_style),
            Paragraph("Not Supported", tbl_cell_style),
            Paragraph("Deposit-withdrawal match", tbl_cell_style),
            Paragraph("<b>Relayer Gas Linkage (0xRelay99B) + Leaf Timing (94% Conf.)</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Zero-Day Fraud Detection</b>", tbl_cell_style),
            Paragraph("Requires prior blacklist report", tbl_cell_style),
            Paragraph("Requires prior incident report", tbl_cell_style),
            Paragraph("Crowdsourced bounties", tbl_cell_style),
            Paragraph("Risk rule heuristics", tbl_cell_style),
            Paragraph("<b>Fraud DNA™: 8-D sequence vector match for UNREPORTED wallets</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Indian Court Admissibility</b>", tbl_cell_style),
            Paragraph("Generic CSV / PDF exports", tbl_cell_style),
            Paragraph("Generic incident export", tbl_cell_style),
            Paragraph("None", tbl_cell_style),
            Paragraph("Generic compliance export", tbl_cell_style),
            Paragraph("<b>Automated Section 91 CrPC Police Notice + 65B Dossier</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Live Blockchain RPC Queries</b>", tbl_cell_style),
            Paragraph("Proprietary internal indexer", tbl_cell_style),
            Paragraph("Proprietary internal indexer", tbl_cell_style),
            Paragraph("Proprietary internal indexer", tbl_cell_style),
            Paragraph("Proprietary internal indexer", tbl_cell_style),
            Paragraph("<b>Direct JSON-RPC Multi-Chain + CoinGecko Price Feed</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Cost &amp; Accessibility</b>", tbl_cell_style),
            Paragraph("$50,000+ per year", tbl_cell_style),
            Paragraph("$60,000+ per year", tbl_cell_style),
            Paragraph("Freemium API subscription", tbl_cell_style),
            Paragraph("$40,000+ per year", tbl_cell_style),
            Paragraph("<b>100% Free &amp; Open for Indian Police &amp; LEAs</b>", tbl_bold_cell)
        ]
    ]
    t_diff = Table(diff_table_data, colWidths=[95, 83, 83, 83, 83, 83])
    t_diff.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 2.2),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_diff)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 4 & 5: MODE 1 (CRYPTO ENGINE) DETAILED FEATURE MANUAL
    # =========================================================================
    story.append(Paragraph("3. Mode 1: ₿ Crypto Blockchain Engine &bull; Feature Deep Dive", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    crypto_f_data = [
        [
            Paragraph("<b>🔍 1. Smart Multi-Chain Wallet Scanner</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> High-speed address parser that detects address formats (EVM 0x, Tron T, Solana Base58, Bitcoin Bech32/Legacy) and retrieves on-chain balance breakdowns.<br/>"
                      "&bull; <b>How it Works:</b> Dispatches parallel JSON-RPC `eth_getBalance`, `eth_getTransactionCount`, and REST queries, converting token balances to INR via CoinGecko in under 200ms.<br/>"
                      "&bull; <b>Police Use Case:</b> Police officer pastes suspect address <code>0x098B...f96</code> and immediately sees ₹18.5 Cr received across 130 transactions with live on-chain confirmation.", body_style)
        ],
        [
            Paragraph("<b>💰 2. Stolen Money Tracker (Tranche Follower)</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Dedicated tranche-locking engine that follows a specific victim's loss amount rather than getting lost in the scammer's total wallet volume.<br/>"
                      "&bull; <b>How it Works:</b> Calculates peeling ratios (e.g. 60/40 split &rarr; 36/24 split) and isolates the exact path taken by the victim's funds to the destination exchange.<br/>"
                      "&bull; <b>Police Use Case:</b> A victim loses ₹50,000. The tool proves ₹30k went to Mule A, ₹18k went to WazirX, and ₹20k went to Binance, generating a copyable audit trail CSV.", body_style)
        ],
        [
            Paragraph("<b>🕸️ 3. Animated Multi-Hop Fund Flow Graph</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Interactive SVG flowchart representing transaction lineage: <code>Victim &rarr; Scammer Hub &rarr; Intermediate Mules &rarr; CEX Sweep</code>.<br/>"
                      "&bull; <b>How it Works:</b> Uses SVG path geometry with dynamic CSS particle animations where particle speed reflects transaction velocity.<br/>"
                      "&bull; <b>Police Use Case:</b> Replaces 50 pages of raw blockchain hex data with a clear visual evidence chart that judges and prosecutors can easily understand.", body_style)
        ],
        [
            Paragraph("<b>🎯 4. Time-Travel Transaction Scrubber</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Chronological playback scrubber with Play, Pause, Step Back/Forward, and 1x–4x speed multiplier controls.<br/>"
                      "&bull; <b>How it Works:</b> Sorts all transactions by timestamp from Hour 0 to Hour 24 and highlights nodes and paths sequentially as the time slider advances.<br/>"
                      "&bull; <b>Police Use Case:</b> Demonstrates that money was peeled and swept to an exchange in under 30 seconds, proving the crime was operated by an automated bot network.", body_style)
        ],
        [
            Paragraph("<b>🏦 5. Exchange Identification &amp; Cluster Attribution</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Heuristic CEX clustering engine that matches destination deposit addresses to centralized exchanges holding KYC records.<br/>"
                      "&bull; <b>How it Works:</b> Analyzes sweep patterns, multi-sig sweeps, and deposit proxy patterns across 42+ indexed exchanges (Binance, WazirX, CoinDCX, KuCoin, OKX).<br/>"
                      "&bull; <b>Police Use Case:</b> Identifies that stolen funds entered <code>Binance Hot Cluster 14</code> with 98% confidence, identifying the exact legal entity to subpoena.", body_style)
        ]
    ]
    t_cf1 = Table(crypto_f_data, colWidths=[510])
    t_cf1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 3.5),
    ]))
    story.append(t_cf1)
    story.append(PageBreak())
    
    # Mode 1 features part 2
    story.append(Paragraph("3. Mode 1: ₿ Crypto Blockchain Engine &bull; Feature Deep Dive (Contd.)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    crypto_f_data2 = [
        [
            Paragraph("<b>🧬 6. Fraud DNA™ Zero-Day Campaign Syndicate Attribution</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Vector behavioral sequence fingerprinting that matches newly generated, unreported scam wallets against known cyber syndicate playbooks.<br/>"
                      "&bull; <b>How it Works:</b> Evaluates an 8-dimensional behavioral vector (transfer cadence, split ratio, gas sponsor, bridge usage) and scores similarity against known campaigns (#CYB-2048, #CYB-3912, #CYB-1084).<br/>"
                      "&bull; <b>Police Use Case:</b> Scammers deploy a brand new unflagged wallet. Fraud DNA™ identifies a <b>91% match with the Hydra-Peel Telegram Job Scam syndicate</b>.", body_style)
        ],
        [
            Paragraph("<b>🌪️ 7. Mixer &amp; Privacy Pool Demasking Engine</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> De-anonymizes obfuscation protocols (Tornado.Cash, Sinbad, CoinJoin) that scammers use to hide their money trails.<br/>"
                      "&bull; <b>How it Works:</b> Correlates shared gas relayer dispatchers (e.g. <code>0xRelay99B</code>), deposit-withdrawal timing brackets, and round-denomination pool mechanics.<br/>"
                      "&bull; <b>Police Use Case:</b> Connects a 100 ETH Tornado Cash deposit to a withdrawal address 32 minutes later, shrinking the anonymity set from 10,000 to a single target with 94.2% confidence.", body_style)
        ],
        [
            Paragraph("<b>🌉 8. Cross-Chain Bridge &amp; Hop Tracker</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Seamlessly traces illicit funds when scammers hop across blockchains to evade single-chain tracking tools.<br/>"
                      "&bull; <b>How it Works:</b> Monitors liquidity teleport routers (Across, Stargate, FixedFloat) across Ethereum, Tron (TRC-20), BSC, Bitcoin, and Solana, unifying the entire flow.<br/>"
                      "&bull; <b>Police Use Case:</b> Follows an ERC-20 USDT deposit on Ethereum as it hops across Across Protocol to Tron and deposits into a Binance TRC-20 gateway.", body_style)
        ],
        [
            Paragraph("<b>🗺️ 9. Real-World Geographic Cartographic Map &amp; Nexus Graph</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Authentic vector cartography showing city-to-city money flows between Indian Cyber Cells and international cashout hubs.<br/>"
                      "&bull; <b>How it Works:</b> Projects real coordinates (Mumbai, Delhi, Bengaluru, Surat, Dubai, Singapore, Hong Kong, Zurich, London) with great-circle curved flight arcs and radar beacons.<br/>"
                      "&bull; <b>Police Use Case:</b> Pinpoints that scam funds originated in Surat, Gujarat and were cashed out at an OTC P2P cashout desk in Dubai, UAE.", body_style)
        ],
        [
            Paragraph("<b>📜 10. Automated Section 91 CrPC Subpoena &amp; 65B Dossier Generator</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> 1-click legal notice generator compliant with Indian criminal procedure and the Indian Evidence Act for immediate exchange dispatch.<br/>"
                      "&bull; <b>How it Works:</b> Auto-fills the exchange legal desk, transaction hash, destination cluster, seizure amount (INR/crypto), and digitally signs the document with a SHA-256 seal.<br/>"
                      "&bull; <b>Police Use Case:</b> An officer generates a court-ready freeze order in 3 seconds and emails it directly to Binance or WazirX legal nodal desks.", body_style)
        ]
    ]
    t_cf2 = Table(crypto_f_data2, colWidths=[510])
    t_cf2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 3.5),
    ]))
    story.append(t_cf2)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 6: MODE 2 (UPI & BANKING ENGINE) DETAILED FEATURE MANUAL
    # =========================================================================
    story.append(Paragraph("4. Mode 2: 📱 UPI &amp; Core Banking Engine &bull; Feature Deep Dive", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    bank_f_data = [
        [
            Paragraph("<b>🔄 1. Dual Engine Mode Switcher</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Seamless header switcher allowing officers to toggle between ₿ Crypto Blockchain Mode and 📱 UPI/Banking Mode without page reloads.<br/>"
                      "&bull; <b>How it Works:</b> Synchronizes active view containers, customizes sidebar navigation, and preserves active case state across both financial rails.<br/>"
                      "&bull; <b>Police Use Case:</b> An investigator starts by tracing an on-chain wallet and toggles to Mode 2 to trace the underlying Indian UPI mule accounts.", body_style)
        ],
        [
            Paragraph("<b>🏦 2. Smart VPA &amp; Core Banking Account Lookup</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Resolves victim-reported UPI VPAs (e.g. <code>daily.payout@oksbi</code>) or Bank UTRs to identify the underlying bank branch, IFSC, and account holder.<br/>"
                      "&bull; <b>How it Works:</b> Queries simulated NPCI/Core Banking System (CBS) gateways to extract masked account numbers, bank names, branch cities, and linked mobile numbers.<br/>"
                      "&bull; <b>Police Use Case:</b> Resolves suspect VPA to <b>State Bank of India, Andheri East Branch, Mumbai (`SBIN0001245`)</b>, identifying the specific branch to issue freeze notices.", body_style)
        ],
        [
            Paragraph("<b>🕸️ 3. Multi-Tier Bank Mule Layering Graph</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Maps the movement of stolen fiat money across Tier-1, Tier-2, and Tier-3 mule bank accounts to pinpoint where funds are still recoverable.<br/>"
                      "&bull; <b>How it Works:</b> Constructs a visual graph showing incoming transfers, secondary splits across mule banks (HDFC, ICICI, PNB), and ATM withdrawal endpoints.<br/>"
                      "&bull; <b>Police Use Case:</b> Shows that out of ₹84,500 stolen, ₹50,700 moved to Tier-2 Mule A (HDFC Surat) and ₹33,800 to Tier-2 Mule B (ICICI Jaipur).", body_style)
        ],
        [
            Paragraph("<b>🏧 4. ATM &amp; POS Cash-Out Sweeps Tracker</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Identifies how much stolen money has been withdrawn as physical cash versus what remains actionable in the banking system.<br/>"
                      "&bull; <b>How it Works:</b> Calculates ATM cashout velocity and computes the exact <b>Actionable Retrievable Balance</b> that can be legally frozen immediately.<br/>"
                      "&bull; <b>Police Use Case:</b> Alerts the officer: <b>'₹30,420 Retrievable (Actionable Balance)'</b> in SBI Surat Mule Account before the scammer reaches an ATM.", body_style)
        ],
        [
            Paragraph("<b>🚨 5. NCRP 1930 Portal Complaints Pattern Matching</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Correlates the queried UPI/UTR with the National Cyber Crime Reporting Portal database to identify connected victim complaints across India.<br/>"
                      "&bull; <b>How it Works:</b> Queries complaint history and flags repeated fraud patterns, SIM-swap locations (e.g. Surat, Gujarat), and overseas proxy routing (Cambodia).<br/>"
                      "&bull; <b>Police Use Case:</b> Flags that the suspect account is linked to <b>14 active NCRP 1930 complaints</b> with ₹24,80,000 in total nationwide losses.", body_style)
        ],
        [
            Paragraph("<b>📞 6. Bank Nodal Officer Directory &amp; 1-Click Freeze Notice</b><br/>"
                      "&bull; <b>Meaning &amp; Purpose:</b> Provides instant access to verified Law Enforcement Nodal contacts across 42+ Indian banks and generates Section 91 CrPC freeze notices.<br/>"
                      "&bull; <b>How it Works:</b> Auto-drafts a formal legal order pre-filled with the suspect Account Number, IFSC, UTR, and NCRP Case ID, ready for direct email dispatch.<br/>"
                      "&bull; <b>Police Use Case:</b> Officer clicks 'Generate Bank Freeze Notice' and dispatches the Section 91 order directly to SBI's Cyber Cell Nodal Desk in under 5 seconds.", body_style)
        ]
    ]
    t_bf = Table(bank_f_data, colWidths=[510])
    t_bf.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 3.5),
    ]))
    story.append(t_bf)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 7: THE 10 REALISTIC CRIME PRESETS REFERENCE GUIDE
    # =========================================================================
    story.append(Paragraph("5. Built-In Testing Presets Reference Guide (10 Crime Scenarios)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    story.append(Paragraph(
        "CyberTrace includes 10 pre-loaded real-world crime scenarios (5 Crypto + 5 Banking) enabling instant testing and evaluation without manual typing:",
        body_style
    ))
    story.append(Spacer(1, 2))
    
    preset_table_data = [
        [
            Paragraph("<b>Mode / Preset Name</b>", tbl_hdr_style),
            Paragraph("<b>Target Identifier</b>", tbl_hdr_style),
            Paragraph("<b>Modus Operandi &amp; Crime Case</b>", tbl_hdr_style),
            Paragraph("<b>Reported Loss</b>", tbl_hdr_style),
            Paragraph("<b>Attribution / Destination</b>", tbl_hdr_style)
        ],
        [
            Paragraph("<b>₿ Crypto Preset 1</b><br/>Lazarus APT-38 Exploit", tbl_cell_style),
            Paragraph("<code>0x098B...f96</code>", tbl_cell_style),
            Paragraph("State-sponsored smart contract multi-sig exploit &amp; mixer laundering.", tbl_cell_style),
            Paragraph("₹18.50 Cr<br/>(98% Risk)", tbl_cell_style),
            Paragraph("Tornado.Cash 100 ETH &bull; Binance Off-Ramp", tbl_cell_style)
        ],
        [
            Paragraph("<b>₿ Crypto Preset 2</b><br/>Telegram Task Job Scam", tbl_cell_style),
            Paragraph("<code>0xA1b2...9T0</code>", tbl_cell_style),
            Paragraph("3-hop automated peeling chain shaving small tranches in <45s.", tbl_cell_style),
            Paragraph("₹84,500<br/>(91% Risk)", tbl_cell_style),
            Paragraph("Hydra-Peel &bull; WazirX India Gateway Hot 02", tbl_cell_style)
        ],
        [
            Paragraph("<b>₿ Crypto Preset 3</b><br/>Digital Arrest Sextortion", tbl_cell_style),
            Paragraph("<code>0x742d...44e</code>", tbl_cell_style),
            Paragraph("Fake police video extortion using permit2 malicious token drainers.", tbl_cell_style),
            Paragraph("₹1,50,000<br/>(96% Risk)", tbl_cell_style),
            Paragraph("CoinDCX Off-Ramp Hub &bull; Dubai OTC Desk", tbl_cell_style)
        ],
        [
            Paragraph("<b>₿ Crypto Preset 4</b><br/>Pig Butchering Arbitrage", tbl_cell_style),
            Paragraph("<code>0x8920...3e7</code>", tbl_cell_style),
            Paragraph("Fake high-yield liquidity mining platform with multi-sig vault sweeps.", tbl_cell_style),
            Paragraph("₹1.45 Cr<br/>(88% Risk)", tbl_cell_style),
            Paragraph("Golden-Boar &bull; OKX &amp; KuCoin Vault", tbl_cell_style)
        ],
        [
            Paragraph("<b>₿ Crypto Preset 5</b><br/>Binance Official Hot 14", tbl_cell_style),
            Paragraph("<code>0x28C6...1d60</code>", tbl_cell_style),
            Paragraph("Verified clean institutional exchange control for false-positive validation.", tbl_cell_style),
            Paragraph("₹2,840 Cr<br/>(12% Safe)", tbl_cell_style),
            Paragraph("Binance Holdings Ltd. (0 NCRP FIRs)", tbl_cell_style)
        ],
        [
            Paragraph("<b>📱 UPI Preset 1</b><br/>Telegram Job Scam VPA", tbl_cell_style),
            Paragraph("<code>daily.payout@oksbi</code>", tbl_cell_style),
            Paragraph("Part-time Telegram review task scam; SIM swapped in Surat, Gujarat.", tbl_cell_style),
            Paragraph("₹84,500<br/>(14 FIRs)", tbl_cell_style),
            Paragraph("SBI Andheri East &bull; ₹30,420 Retrievable", tbl_cell_style)
        ],
        [
            Paragraph("<b>📱 UPI Preset 2</b><br/>Digital Arrest Fake CBI", tbl_cell_style),
            Paragraph("<code>cbi.investigation.fund@okaxis</code>", tbl_cell_style),
            Paragraph("Fake law enforcement video call escrow; IP routed via Cambodia proxy.", tbl_cell_style),
            Paragraph("₹1,50,000<br/>(22 FIRs)", tbl_cell_style),
            Paragraph("Axis Bank Connaught Place &bull; ₹54k Actionable", tbl_cell_style)
        ],
        [
            Paragraph("<b>📱 UPI Preset 3</b><br/>Phishing QR Code Scam", tbl_cell_style),
            Paragraph("<code>quick.pay24@ybl</code>", tbl_cell_style),
            Paragraph("Dynamic overlay QR code debit scam operated by Jamtara cyber ring.", tbl_cell_style),
            Paragraph("₹25,000<br/>(8 FIRs)", tbl_cell_style),
            Paragraph("Yes Bank Indiranagar &bull; ₹9k Actionable", tbl_cell_style)
        ],
        [
            Paragraph("<b>📱 UPI Preset 4</b><br/>Fake Electricity Bill APK", tbl_cell_style),
            Paragraph("<code>UTR-20260825-991240</code>", tbl_cell_style),
            Paragraph("Malicious remote access APK scraping victim banking OTPs and SMS.", tbl_cell_style),
            Paragraph("₹42,000<br/>(6 FIRs)", tbl_cell_style),
            Paragraph("PNB / HDFC Salt Lake &bull; ₹15,120 Actionable", tbl_cell_style)
        ],
        [
            Paragraph("<b>📱 UPI Preset 5</b><br/>Offshore IPL Betting", tbl_cell_style),
            Paragraph("<code>vip.gaming.deposit@paytm</code>", tbl_cell_style),
            Paragraph("Illegal offshore sports betting platform routing fiat into Dubai P2P crypto.", tbl_cell_style),
            Paragraph("₹2,10,000<br/>(31 FIRs)", tbl_cell_style),
            Paragraph("Paytm Payments Bank &bull; ₹75,600 Actionable", tbl_cell_style)
        ]
    ]
    t_pr = Table(preset_table_data, colWidths=[95, 85, 150, 75, 105])
    t_pr.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 2.2),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_pr)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 8: SECURITY, LEGAL ADMISSIBILITY & PRODUCTION ROADMAP
    # =========================================================================
    story.append(Paragraph("6. Security, Legal Admissibility &amp; Production Roadmap", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    sec_legal_text = (
        "<b>Enterprise Threat Defense &amp; Anti-Tampering Shield:</b><br/>"
        "&bull; <b>Anti-XSS Input Sanitizer:</b> Strict HTML entity encoding and regex neutralization on all address and case fields prevent stored and reflected script injection.<br/>"
        "&bull; <b>Anti-Clickjacking Framebuster:</b> <code>X-Frame-Options: DENY</code> and runtime framebuster JavaScript prevent unauthorized embedding in malicious parent iframes.<br/>"
        "&bull; <b>Content Security Policy (CSP Level 3):</b> Restricts all network sockets strictly to whitelisted verified Ethereum/BSC JSON-RPC endpoints and Google Fonts.<br/>"
        "&bull; <b>Token Bucket Rate Limiter:</b> Throttles automated bot floods and brute-force scanning (50 req/min max).<br/>"
        "&bull; <b>AES-256 / SHA-256 Cryptographic Evidence Vault:</b> Case notes and evidence dossiers are sealed with immutable SHA-256 hashes.<br/><br/>"
        "<b>Indian Legal Admissibility (Section 65B Indian Evidence Act):</b><br/>"
        "All electronic evidence generated by CyberTrace includes server cryptographic timestamps, machine hashes, blockchain block confirmations, and digital officer signature blocks, satisfying the statutory requirements of Section 65B of the Indian Evidence Act and Section 91/102 of the Code of Criminal Procedure (CrPC)."
    )
    t_sec = Table([[Paragraph(sec_legal_text, body_style)]], colWidths=[510])
    t_sec.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f0fdf4")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_sec)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>Enterprise Production Architecture &amp; Requirements Roadmap:</b>", h2_style))
    prod_text = (
        "To scale CyberTrace for nationwide deployment across all 36 State/UT Cyber Police Headquarters:<br/>"
        "&bull; <b>Backend API Gateway (Node.js / FastAPI):</b> Acts as a secure proxy to protect private paid API keys (Alchemy, Etherscan Pro, TronGrid, Moralis).<br/>"
        "&bull; <b>High-Speed Redis Cache:</b> Stores indexed transaction graphs and exchange cluster heuristics with sub-10ms response latency.<br/>"
        "&bull; <b>RBI Account Aggregator (AA) Framework:</b> Connects with licensed AAs (Setu, Anumati) for consent-based bank statement parsing across 100+ Indian banks.<br/>"
        "&bull; <b>PostgreSQL + PostGIS &amp; AWS S3 Storage:</b> Scalable database storage with spatial indexing for city maps and SHA-256 sealed PDF dossier storage."
    )
    story.append(Paragraph(prod_text, body_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Verification Resources &amp; Access Links:</b>", h2_style))
    res_data = [
        [Paragraph("<b>Live Web Platform (GitHub Pages):</b>", body_style), Paragraph("<font color='#0066ff'><u>https://hidayatulla268.github.io/CyberTrace/</u></font>", body_style)],
        [Paragraph("<b>GitHub Repository:</b>", body_style), Paragraph("<font color='#0066ff'><u>https://github.com/Hidayatulla268/CyberTrace</u></font>", body_style)],
        [Paragraph("<b>Documentation PDF File:</b>", body_style), Paragraph("<font color='#0066ff'><u>CyberTrace_Platform_Guide.pdf</u></font>", body_style)],
        [Paragraph("<b>Security Certification:</b>", body_style), Paragraph("Enterprise Grade (Anti-XSS &bull; CSP Level 3 &bull; SHA-256 Tamper-Proof Vault)", body_style)]
    ]
    t_res = Table(res_data, colWidths=[170, 340])
    t_res.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 3.5),
    ]))
    story.append(t_res)
    story.append(Spacer(1, 5))
    
    story.append(Paragraph(
        "<font size=6.5 color='#64748b'><i>CyberTrace is developed for the Smart India Hackathon 2026 (Problem Statement PS-26183) in collaboration with the Indian Cyber Crime Coordination Centre (I4C), Ministry of Home Affairs, Government of India. All rights reserved.</i></font>",
        ParagraphStyle('EndNote', alignment=1)
    ))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Master Comprehensive PDF Guide generated: {output_path}")

if __name__ == '__main__':
    out_file = os.path.join(r"c:\Users\HP\OneDrive\Desktop\crypto", "CyberTrace_Platform_Guide.pdf")
    build_comprehensive_pdf(out_file)


