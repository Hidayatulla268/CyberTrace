"""
CyberTrace - PDF Documentation Generator
Creates a publication-quality comprehensive PDF guide for CyberTrace (SIH 2026 PS-26183).
"""

import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
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
            return  # Suppress headers/footers on cover page
        
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header
        self.drawString(54, 11 * 72 - 36, "CYBERTRACE &bull; CRYPTO FORENSICS PLATFORM (SIH 2026 PS-26183)")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 11 * 72 - 42, 8.5 * 72 - 54, 11 * 72 - 42)
        
        # Footer
        self.setFont("Helvetica", 8)
        self.drawString(54, 36, "Confidential — Indian Cyber Crime Coordination Centre (I4C) / MHA")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * 72 - 54, 36, page_text)
        self.line(54, 46, 8.5 * 72 - 54, 46)
        self.restoreState()

def create_cybertrace_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Brand Colors
    c_primary = colors.HexColor("#0066ff")
    c_dark = colors.HexColor("#060d1f")
    c_accent = colors.HexColor("#00c0ff")
    c_purple = colors.HexColor("#8b5cf6")
    c_amber = colors.HexColor("#f59e0b")
    c_red = colors.HexColor("#ef4444")
    c_green = colors.HexColor("#10b981")
    c_card_bg = colors.HexColor("#f8fafc")
    c_border = colors.HexColor("#e2e8f0")
    
    # Typography Styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=colors.HexColor("#0f172a"),
        alignment=0
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=18,
        textColor=colors.HexColor("#475569")
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=14,
        spaceAfter=6
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=c_primary,
        spaceBefore=10,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6
    )
    
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155"),
        leftIndent=14,
        spaceAfter=3
    )
    
    badge_style = ParagraphStyle(
        'BadgeText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )
    
    story = []
    
    # ==========================================
    # COVER PAGE
    # ==========================================
    story.append(Spacer(1, 20))
    story.append(Paragraph("🛡️ <b>CYBERTRACE</b>", ParagraphStyle('LogoText', fontName='Helvetica-Bold', fontSize=22, textColor=c_primary, leading=26)))
    story.append(Paragraph("Real-Time Identification of Fraud-Linked Cryptocurrency Exchanges from Victim-Reported Suspect Wallet Addresses through Automated Blockchain Analytics", title_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Smart India Hackathon 2026 &bull; Problem Statement PS-26183</b><br/>Indian Cyber Crime Coordination Centre (I4C) &bull; Ministry of Home Affairs, Government of India", subtitle_style))
    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=2, color=c_primary, spaceBefore=5, spaceAfter=15))
    
    # Metadata Box
    meta_data = [
        [Paragraph("<b>Platform:</b> CyberTrace Automated Analytics Engine", body_style), Paragraph("<b>Target Focus:</b> PS-26183 Solution Suite", body_style)],
        [Paragraph("<b>Author / Lead:</b> Shaik Hidayatulla", body_style), Paragraph("<b>Version:</b> 2.0 Production Ready", body_style)],
        [Paragraph("<b>Repository:</b> github.com/Hidayatulla268/CyberTrace", body_style), Paragraph("<b>Live Demo:</b> hidayatulla268.github.io/CyberTrace/", body_style)]
    ]
    t_meta = Table(meta_data, colWidths=[250, 250])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 20))
    
    # Executive Summary Card
    exec_summary_text = (
        "<b>Executive Summary:</b><br/>"
        "Cyber fraud victims increasingly report suspect cryptocurrency wallet addresses used by fraudsters in cases involving "
        "<b>task-based scams, sextortion, ransomware, phishing, fake job rackets, and organized cyber-enabled financial crimes</b>. "
        "CyberTrace solves this challenge through an end-to-end automated platform providing real-time multi-hop blockchain tracing, "
        "heuristic AI risk scoring, Centralized Exchange (CEX) attribution, zero-day Fraud DNA™ campaign matching, and "
        "court-ready Section 91 CrPC legal dossiers."
    )
    t_exec = Table([[Paragraph(exec_summary_text, body_style)]], colWidths=[500])
    t_exec.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#e0f2fe")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#38bdf8")),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(t_exec)
    
    story.append(Spacer(1, 25))
    
    # Core USP Banner
    story.append(Paragraph("⭐ <b>THE CORE FORENSIC WORKFLOW (USP)</b>", h2_style))
    usp_steps = [
        [
            Paragraph("<font color='#0066ff'><b>1. REPORT</b></font><br/><font size=7.5 color='#475569'>Victim Intake</font>", ParagraphStyle('U1', fontName='Helvetica-Bold', fontSize=8.5, alignment=1, leading=11)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=12, alignment=1)),
            Paragraph("<font color='#0066ff'><b>2. TRACE</b></font><br/><font size=7.5 color='#475569'>Stolen Funds</font>", ParagraphStyle('U2', fontName='Helvetica-Bold', fontSize=8.5, alignment=1, leading=11)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=12, alignment=1)),
            Paragraph("<font color='#0066ff'><b>3. CONNECT</b></font><br/><font size=7.5 color='#475569'>Hidden Wallets</font>", ParagraphStyle('U3', fontName='Helvetica-Bold', fontSize=8.5, alignment=1, leading=11)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=12, alignment=1)),
            Paragraph("<font color='#0066ff'><b>4. IDENTIFY</b></font><br/><font size=7.5 color='#475569'>Exchange CEX</font>", ParagraphStyle('U4', fontName='Helvetica-Bold', fontSize=8.5, alignment=1, leading=11)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=12, alignment=1)),
            Paragraph("<font color='#0066ff'><b>5. MONITOR</b></font><br/><font size=7.5 color='#475569'>Live Mempool</font>", ParagraphStyle('U5', fontName='Helvetica-Bold', fontSize=8.5, alignment=1, leading=11)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=12, alignment=1)),
            Paragraph("<font color='#0066ff'><b>6. PROVE</b></font><br/><font size=7.5 color='#475569'>I4C Dossier</font>", ParagraphStyle('U6', fontName='Helvetica-Bold', fontSize=8.5, alignment=1, leading=11))
        ]
    ]
    t_usp = Table(usp_steps, colWidths=[65, 15, 65, 15, 65, 15, 65, 15, 65, 15, 65])
    t_usp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_usp)
    story.append(PageBreak())
    
    # ==========================================
    # SECTION 1: PROBLEM STATEMENT & MOTIVATION
    # ==========================================
    story.append(Paragraph("1. Smart India Hackathon PS-26183 Context", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=8))
    
    story.append(Paragraph(
        "<b>Background:</b> When cyber fraud victims lose funds to investment scams, task-based frauds, sextortion, ransomware, or phishing, "
        "the funds are swiftly transferred into cryptocurrencies. Fraudsters employ automated peeling chains, sub-minute splits, and intermediary layering "
        "wallets before depositing funds into Centralized Exchanges (CEXs) like Binance, WazirX, CoinDCX, KuCoin, or laundering through mixers.",
        body_style
    ))
    story.append(Paragraph(
        "<b>The Operational Challenge for Law Enforcement:</b><br/>"
        "1. <i>Velocity:</i> Funds move across 3 to 5 hops within minutes of victim reporting.<br/>"
        "2. <i>Exchange Obfuscation:</i> Identifying whether an address is an intermediary or a known exchange hot-wallet requires multi-sig cluster heuristics.<br/>"
        "3. <i>Zero-Day Wallets:</i> New fraudulent wallets that have not yet been reported on the 1930 portal escape traditional blacklist detection.<br/>"
        "4. <i>Evidentiary Friction:</i> Investigators need structured, hash-verified Section 91 CrPC legal notices to freeze accounts before cash-out.",
        body_style
    ))
    story.append(Spacer(1, 8))
    
    # ==========================================
    # SECTION 2: MASTER FEATURE SUITE
    # ==========================================
    story.append(Paragraph("2. Comprehensive Feature Suite (13 Key Capabilities)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=8))
    
    features_list = [
        ("🔍 Smart Wallet Scanner", "Instant multi-chain address scanner aggregating token balances (USDT, ETH, BTC, TRX, INR Equiv.), activity timelines, and full blockchain transaction ledgers."),
        ("💰 Stolen Money Tracker", "Interactive tranche follower that selects a victim deposit transaction (e.g. ₹50,000) and follows that exact money hop-by-hop across peeling splits (60%/40% -> 36%/24%) with CSV export."),
        ("🕸️ Fund-Flow Graph", "Interactive SVG visualizer mapping Victim -> Suspect -> Intermediary Splitters -> Exchange Clusters with live animated particle flows and node inspection."),
        ("🏦 Exchange Finder", "Automated attribution of destination Centralized Exchanges (Binance Hot 14, WazirX, KuCoin, OKX) with confidence metrics (e.g. 91% Confidence) and legal nodal officer records."),
        ("🔗 Hidden Wallet Detector", "Discovers unlisted accomplice infrastructure connected to the suspect, including Gas Sponsor Relayers, Co-Spending Mules, and Peeling Splitters with 1-click tracing."),
        ("🚨 Heuristic Risk Score", "Dynamic 0–100 AI threat gauge categorizing wallets into Low, Medium, High, or Critical risk with clear forensic evidence bullet points."),
        ("🧠 Fraud Pattern Detection", "Automated recognition of peeling chains, sub-45s script sweeps, fan-out/fan-in layering, and smart contract mixer calls."),
        ("🧬 Fraud DNA™ Detection", "Breakthrough behavioral vector matching engine that identifies zero-day unknown scam wallets based on campaign DNA (91% match with Campaign #CYB-2048)."),
        ("⏱️ Live Wallet Monitoring", "Real-time mempool transaction ingestion stream with live pulse indicators, pause/resume controls, and instant threat alert triggers."),
        ("📋 Fraud Reporting Portal", "Victim complaint intake portal that accepts TXID, wallet address, amount, and scam type, auto-generating an FIR reference ID and immediately initiating trace flows."),
        ("🧾 Auto Evidence Report", "1-click generation of court-ready Section 91 CrPC forensic dossiers containing full suspect metadata, flow graphs, timestamps, and SHA-256 integrity stamps."),
        ("🌐 Public Safety Check", "Consumer pre-transaction scam screener providing instant SAFE, CAUTION, or ⛔ DO NOT SEND verdicts to prevent fraud before users send funds."),
        ("🕵️ Fraud Network Map", "Cross-case crime syndicate graph correlating multiple independent victim complaints into an interconnected multi-case laundering nexus.")
    ]
    
    f_table_data = [[Paragraph(f"<b>{title}</b>", ParagraphStyle('FT', fontName='Helvetica-Bold', fontSize=8.5, textColor=c_primary)), Paragraph(desc, body_style)] for title, desc in features_list]
    t_feat = Table(f_table_data, colWidths=[150, 350])
    t_feat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_feat)
    story.append(PageBreak())
    
    # ==========================================
    # SECTION 3: DEEP DIVE — FRAUD DNA™
    # ==========================================
    story.append(Paragraph("3. Fraud DNA™ — Detecting Scam Networks from Unknown Wallets", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=8))
    
    story.append(Paragraph(
        "<b>The Core Innovation:</b> Traditional cybercrime tools rely on static blacklists. If a fraudster creates a new, unreported wallet (Wallet Z), blacklists give it a clean rating. "
        "<b>Fraud DNA™</b> analyzes the mathematical and behavioral sequence of transactions to identify if an unknown wallet behaves like a known crime syndicate.",
        body_style
    ))
    
    dna_flow_text = (
        "<b>BEHAVIORAL LINEAGE RECONSTRUCTION:</b><br/>"
        "KNOWN FRAUD DNA &rarr; Wallet A (Victim 1 Hub) & Wallet B (Victim 2 Hub) &rarr; Synthesized Fraud Pattern &rarr; <b>🆕 Unreported Candidate Wallet Z (91% Match)</b><br/><br/>"
        "<b>Display Alert:</b><br/>"
        "<font color='#dc2626'><b>🔴 Potential Unreported Fraud Wallet Detected</b></font><br/>"
        "&bull; <b>Wallet:</b> 0xAB89C41d2E5F78a9B30C2d4E6F8a91F2<br/>"
        "&bull; <b>Fraud DNA Match:</b> 91% Confidence<br/>"
        "&bull; <b>Attributed Campaign:</b> Campaign #CYB-2048 (\"Hydra-Peel\" Telegram Scam)<br/>"
        "&bull; <b>Forensic Evidence:</b> Similar 80/20 tranche split, sub-45s script delay, Binance sweep gateway, connected to 2nd-degree syndicate child node."
    )
    t_dna = Table([[Paragraph(dna_flow_text, body_style)]], colWidths=[500])
    t_dna.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#fef2f2")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#fca5a5")),
        ('PADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_dna)
    story.append(Spacer(1, 10))
    
    # 8-Dimension Vector Radar Table
    story.append(Paragraph("<b>8-Dimensional Behavioral Vector Profile:</b>", h2_style))
    vec_data = [
        [Paragraph("<b>Vector Dimension</b>", body_style), Paragraph("<b>Analyzed Trait & Pattern</b>", body_style), Paragraph("<b>Weight</b>", body_style)],
        [Paragraph("1. Transfer Cadence", body_style), Paragraph("Automated script execution velocity (<45s per hop)", body_style), Paragraph("94%", body_style)],
        [Paragraph("2. Peeling Ratio", body_style), Paragraph("Exact 80/20 & 60/40 fund-splitting tranche distribution", body_style), Paragraph("92%", body_style)],
        [Paragraph("3. Hop Topology", body_style), Paragraph("3-to-4 tier intermediary fan-out depth before sweep", body_style), Paragraph("96%", body_style)],
        [Paragraph("4. Tranche Sizing", body_style), Paragraph("Average victim tranche profile matching ₹20k–₹1L", body_style), Paragraph("88%", body_style)],
        [Paragraph("5. Destination Cluster", body_style), Paragraph("Consolidation into Binance Hot Cluster 14 gateway", body_style), Paragraph("91%", body_style)],
        [Paragraph("6. Gas Sponsorship", body_style), Paragraph("Shared relayer dispatcher funding gas via FixedFloat", body_style), Paragraph("86%", body_style)]
    ]
    t_vec = Table(vec_data, colWidths=[130, 310, 60])
    t_vec.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_vec)
    story.append(Spacer(1, 15))
    
    # ==========================================
    # SECTION 4: LAW ENFORCEMENT & LEGAL COMPLIANCE
    # ==========================================
    story.append(Paragraph("4. Law Enforcement Legal Compliance (Section 91 CrPC)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=8))
    story.append(Paragraph(
        "CyberTrace is designed to bridge the gap between blockchain analytics and courtroom admissibility under Indian law: "
        "<br/>&bull; <b>Section 91 CrPC Subpoena Automation:</b> Automatically drafts emergency freeze notices with exchange deposit memos and TXIDs."
        "<br/>&bull; <b>Chain of Custody & Hash Integrity:</b> All generated evidence reports include SHA-256 cryptographic verification stamps."
        "<br/>&bull; <b>Exchange Nodal Liaison:</b> Pre-mapped direct law enforcement desk emails for Binance, CoinDCX, WazirX, KuCoin, and OKX.",
        body_style
    ))
    story.append(PageBreak())
    
    # ==========================================
    # SECTION 5: LIVE DEMO & JUDGES WALKTHROUGH
    # ==========================================
    story.append(Paragraph("5. Step-by-Step Judges Live Demo Walkthrough", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("To evaluate CyberTrace in a hackathon or live investigation setting, follow the 7-step guided demo:", body_style))
    
    demo_steps_data = [
        [Paragraph("<b>Step 1</b>", body_style), Paragraph("<b>Enter Suspect Address</b><br/>Input victim-reported suspect address or select a preset pill (e.g. Case #1245).", body_style)],
        [Paragraph("<b>Step 2</b>", body_style), Paragraph("<b>Trigger Analysis</b><br/>Click 'Analyze' to crawl multi-hop transactions across EVM, Tron, and Bitcoin ledgers.", body_style)],
        [Paragraph("<b>Step 3</b>", body_style), Paragraph("<b>Inspect Risk Score</b><br/>Review the 87/100 High Risk AI gauge and detailed 5-point evidence checklist.", body_style)],
        [Paragraph("<b>Step 4</b>", body_style), Paragraph("<b>Explore Fund-Flow Graph</b><br/>Visually follow funds flowing from Victim -> Suspect -> Intermediaries -> Exchange Cluster.", body_style)],
        [Paragraph("<b>Step 5</b>", body_style), Paragraph("<b>Detect Destination Exchange</b><br/>Identify Centralized Exchange deposit clusters (e.g. Binance Hot 14 with 91% confidence).", body_style)],
        [Paragraph("<b>Step 6</b>", body_style), Paragraph("<b>Fraud DNA™ Zero-Day Test</b><br/>Click preset '🆕 Unreported Wallet Z' to trigger 91% behavioral match with Campaign #CYB-2048.", body_style)],
        [Paragraph("<b>Step 7</b>", body_style), Paragraph("<b>Export Legal Dossier</b><br/>Click 'Generate Dossier' to print the court-ready Section 91 CrPC PDF evidence document.", body_style)]
    ]
    t_demo = Table(demo_steps_data, colWidths=[70, 430])
    t_demo.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_demo)
    story.append(Spacer(1, 15))
    
    # Section 6: Access & Links
    story.append(Paragraph("6. Project Links & Quick Access", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=8))
    
    links_data = [
        [Paragraph("<b>GitHub Repository:</b>", body_style), Paragraph("<font color='#0066ff'><u>https://github.com/Hidayatulla268/CyberTrace</u></font>", body_style)],
        [Paragraph("<b>Live Website (GitHub Pages):</b>", body_style), Paragraph("<font color='#0066ff'><u>https://hidayatulla268.github.io/CyberTrace/</u></font>", body_style)],
        [Paragraph("<b>Contact & Inquiries:</b>", body_style), Paragraph("hidayatullashaik268@gmail.com", body_style)]
    ]
    t_links = Table(links_data, colWidths=[160, 340])
    t_links.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_links)
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated: {output_path}")

if __name__ == '__main__':
    out_file = os.path.join(r"c:\Users\HP\OneDrive\Desktop\crypto", "CyberTrace_Platform_Guide.pdf")
    create_cybertrace_pdf(out_file)
