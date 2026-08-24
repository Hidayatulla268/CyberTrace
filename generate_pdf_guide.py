"""
CyberTrace - Enterprise Forensic Platform PDF Manual Generator
Creates an exhaustive, publication-grade 6-page technical and operational manual for CyberTrace (SIH 2026 PS-26183).
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
        self.drawString(54, 11 * 72 - 36, "CYBERTRACE &bull; ENTERPRISE CRYPTO FORENSICS (SIH 2026 PS-26183)")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 11 * 72 - 42, 8.5 * 72 - 54, 11 * 72 - 42)
        
        # Footer
        self.setFont("Helvetica", 8)
        self.drawString(54, 36, "Confidential — Indian Cyber Crime Coordination Centre (I4C) / Ministry of Home Affairs")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * 72 - 54, 36, page_text)
        self.line(54, 46, 8.5 * 72 - 54, 46)
        self.restoreState()

def build_enterprise_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    c_primary = colors.HexColor("#0066ff")
    c_dark = colors.HexColor("#0f172a")
    
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=c_dark
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11.5,
        leading=16,
        textColor=colors.HexColor("#475569")
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=c_dark,
        spaceBefore=10,
        spaceAfter=4
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14.5,
        textColor=c_primary,
        spaceBefore=7,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=13,
        textColor=colors.HexColor("#334155"),
        spaceAfter=4
    )
    
    story = []
    
    # =========================================================================
    # PAGE 1: COVER & EXECUTIVE PRESENTATION
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("🛡️ <b>CYBERTRACE</b>", ParagraphStyle('LogoText', fontName='Helvetica-Bold', fontSize=22, textColor=c_primary, leading=26)))
    story.append(Paragraph("Enterprise Crypto Forensics &amp; Real-Time Blockchain Analytics Platform", title_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Smart India Hackathon 2026 &bull; Problem Statement PS-26183</b><br/>Indian Cyber Crime Coordination Centre (I4C) &bull; Ministry of Home Affairs, Government of India", subtitle_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=2, color=c_primary, spaceBefore=4, spaceAfter=12))
    
    meta_data = [
        [Paragraph("<b>Platform:</b> CyberTrace Enterprise Engine v2.0", body_style), Paragraph("<b>Global Benchmarks:</b> Chainalysis, TRM Labs, Arkham", body_style)],
        [Paragraph("<b>Author / Lead:</b> Shaik Hidayatulla", body_style), Paragraph("<b>Target Focus:</b> SIH PS-26183 &amp; I4C Law Enforcement", body_style)],
        [Paragraph("<b>GitHub Repository:</b> github.com/Hidayatulla268/CyberTrace", body_style), Paragraph("<b>Live Platform:</b> hidayatulla268.github.io/CyberTrace/", body_style)]
    ]
    t_meta = Table(meta_data, colWidths=[250, 250])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 12))
    
    exec_summary_text = (
        "<b>Executive Summary &amp; Vision:</b><br/>"
        "CyberTrace provides a unified, enterprise-grade blockchain analytics platform matching global capabilities (Chainalysis Reactor, "
        "TRM Labs, Arkham Intelligence, Elliptic) while solving the operational and legal needs of <b>Indian Law Enforcement Agencies (I4C, State Cyber Cells, 1930 Helpline)</b>. "
        "From a single suspect wallet address, the system traces multi-hop peeling chains, detects cross-chain bridge hops, de-anonymizes mixers, correlates syndicate nexus networks, "
        "and generates Section 91 CrPC freeze orders."
    )
    t_exec = Table([[Paragraph(exec_summary_text, body_style)]], colWidths=[500])
    t_exec.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#e0f2fe")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#38bdf8")),
        ('PADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_exec)
    
    story.append(Spacer(1, 14))
    
    # Core USP Banner
    story.append(Paragraph("⭐ <b>THE CORE FORENSIC WORKFLOW (USP)</b>", h2_style))
    usp_steps = [
        [
            Paragraph("<font color='#0066ff'><b>1. REPORT</b></font><br/><font size=7 color='#475569'>Victim Intake</font>", ParagraphStyle('U1', fontName='Helvetica-Bold', fontSize=8, alignment=1, leading=10)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=11, alignment=1)),
            Paragraph("<font color='#0066ff'><b>2. TRACE</b></font><br/><font size=7 color='#475569'>Stolen Funds</font>", ParagraphStyle('U2', fontName='Helvetica-Bold', fontSize=8, alignment=1, leading=10)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=11, alignment=1)),
            Paragraph("<font color='#0066ff'><b>3. CONNECT</b></font><br/><font size=7 color='#475569'>Hidden Wallets</font>", ParagraphStyle('U3', fontName='Helvetica-Bold', fontSize=8, alignment=1, leading=10)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=11, alignment=1)),
            Paragraph("<font color='#0066ff'><b>4. IDENTIFY</b></font><br/><font size=7 color='#475569'>Exchange CEX</font>", ParagraphStyle('U4', fontName='Helvetica-Bold', fontSize=8, alignment=1, leading=10)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=11, alignment=1)),
            Paragraph("<font color='#0066ff'><b>5. MONITOR</b></font><br/><font size=7 color='#475569'>Live Mempool</font>", ParagraphStyle('U5', fontName='Helvetica-Bold', fontSize=8, alignment=1, leading=10)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=11, alignment=1)),
            Paragraph("<font color='#0066ff'><b>6. PROVE</b></font><br/><font size=7 color='#475569'>I4C Dossier</font>", ParagraphStyle('U6', fontName='Helvetica-Bold', fontSize=8, alignment=1, leading=10))
        ]
    ]
    t_usp = Table(usp_steps, colWidths=[65, 15, 65, 15, 65, 15, 65, 15, 65, 15, 65])
    t_usp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 5),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_usp)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 2: PROBLEM STATEMENT & GLOBAL COMPARISON MATRIX
    # =========================================================================
    story.append(Paragraph("1. Problem Statement Background (SIH PS-26183)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    story.append(Paragraph(
        "<b>The Problem:</b> Criminal networks in task-based frauds, sextortion, ransomware, phishing, and fake job rackets "
        "rapidly convert fiat proceeds into cryptocurrencies. Funds are split across 3 to 5 intermediary wallets within minutes and deposited "
        "into Centralized Exchanges (CEXs) to cash out into bank accounts.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Law Enforcement Bottlenecks:</b><br/>"
        "1. <i>Velocity:</i> Laundering scripts execute in <45 seconds, making manual tracing ineffective.<br/>"
        "2. <i>Zero-Day Wallets:</i> Unreported addresses escape traditional blacklists.<br/>"
        "3. <i>Cross-Chain Evasion:</i> Swapping between Ethereum, Tron, and BSC breaks single-chain crawlers.<br/>"
        "4. <i>Legal Friction:</i> Subpoenas under Section 91 CrPC require immediate transaction and memo attribution.",
        body_style
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("2. Global Platform Benchmark Comparison Matrix", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    comp_data = [
        [Paragraph("<b>Capability</b>", body_style), Paragraph("<b>Chainalysis</b>", body_style), Paragraph("<b>TRM Labs</b>", body_style), Paragraph("<b>Arkham</b>", body_style), Paragraph("<b>Elliptic</b>", body_style), Paragraph("<b>CyberTrace</b>", body_style)],
        [Paragraph("Multi-Hop Fund Flow Graph", body_style), Paragraph("Yes", body_style), Paragraph("Yes", body_style), Paragraph("Yes", body_style), Paragraph("Yes", body_style), Paragraph("<b>Yes (SVG+Particles)</b>", body_style)],
        [Paragraph("Time-Travel Scrubber Bar", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("<b>Yes (1x-4x Speed)</b>", body_style)],
        [Paragraph("Cross-Chain Bridge Tracker", body_style), Paragraph("Yes", body_style), Paragraph("Yes", body_style), Paragraph("No", body_style), Paragraph("Yes", body_style), Paragraph("<b>Yes (Across/FixedFloat)</b>", body_style)],
        [Paragraph("100,000+ Entity Directory", body_style), Paragraph("Yes", body_style), Paragraph("Yes", body_style), Paragraph("Yes", body_style), Paragraph("Yes", body_style), Paragraph("<b>Yes (CEX/Mixer/Lazarus)</b>", body_style)],
        [Paragraph("Mixer Demasking (Tornado)", body_style), Paragraph("Partial", body_style), Paragraph("Partial", body_style), Paragraph("No", body_style), Paragraph("Yes", body_style), Paragraph("<b>Yes (Relayer Correlation)</b>", body_style)],
        [Paragraph("OFAC / UN Sanctions Screener", body_style), Paragraph("Yes", body_style), Paragraph("Yes", body_style), Paragraph("No", body_style), Paragraph("Yes", body_style), Paragraph("<b>Yes (Instant AML)</b>", body_style)],
        [Paragraph("Fraud DNA™ (Zero-Day Match)", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("<b>Yes (8-D Vectors)</b>", body_style)],
        [Paragraph("Section 91 CrPC Legal Dossier", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("<b>Yes (Court Admissible)</b>", body_style)],
        [Paragraph("Pre-Transaction Public Screener", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("No", body_style), Paragraph("<b>Yes (Free Citizen Tool)</b>", body_style)],
        [Paragraph("License &amp; Cost", body_style), Paragraph("$50k+/yr", body_style), Paragraph("$60k+/yr", body_style), Paragraph("Freemium", body_style), Paragraph("$40k+/yr", body_style), Paragraph("<b>Free for LEAs</b>", body_style)]
    ]
    t_comp = Table(comp_data, colWidths=[140, 70, 65, 65, 65, 95])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 3.5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_comp)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 3: COMPLETE 20+ FEATURE BREAKDOWN
    # =========================================================================
    story.append(Paragraph("3. Complete Master Feature Suite (20+ Modules)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    f_list = [
        ("🔍 Smart Multi-Chain Scanner", "Aggregates multi-token balances (USDT, ETH, BTC, TRX, INR Equiv.), address tags, and transaction ledgers with copyable hashes."),
        ("💰 Stolen Money Tranche Tracker", "Hop-by-hop tranche tracker following specific victim funds across peeling splits (100% -> 60%/40% -> 36%/24% -> CEX sweep) with CSV export."),
        ("🕸️ Interactive Fund-Flow Graph", "Dynamic SVG graph visually mapping Victim -> Suspect Hub -> Intermediaries -> Exchange Clusters with live particle animations."),
        ("🎯 Time-Travel Playback Scrubber", "Interactive playback bar on the Flow Graph (Play, Pause, Speed 1x-4x, Slider) showing chronological fund movement from Hour 0 to Hour 24."),
        ("🌉 Cross-Chain Bridge Tracker", "Tracks illicit flows hopping across Ethereum, Tron (TRC-20), BSC (BEP-20), Bitcoin, and Solana via Across Protocol, Stargate, and FixedFloat."),
        ("🏷️ 100k+ Entity Directory", "Searchable database indexing CEX deposit hotwallets, privacy mixers, Lazarus Group APT addresses, OTC desks, and darknet marketplaces."),
        ("🌪️ Mixer Demasking Engine", "De-anonymizes Tornado.Cash 10/100 ETH pools through deposit-withdrawal timing correlation and shared gas relayer dispatchers (0xRelay99B)."),
        ("🛡️ Global Sanctions Screener", "Automated compliance screening against US OFAC SDN, UN Sanctions, EU Blacklists, FIU-IND alerts, and INTERPOL Red Notices."),
        ("🔗 Hidden Wallet Detector", "Uncovers unlisted accomplice infrastructure (Gas Sponsors, Co-Spenders, Peeling Splitters) with 1-click 'Trace' routing."),
        ("🚨 Heuristic AI Risk Score", "Dynamic 0–100 AI threat gauge categorizing wallets into Low, Medium, High, or Critical risk with clear forensic evidence bullet points."),
        ("🧠 Fraud Pattern Detection", "Automated recognition of peeling chains, sub-45s script sweeps, fan-out/fan-in layering, and smart contract mixer calls."),
        ("🧬 Fraud DNA™ Syndicate Attribution", "Identifies zero-day unknown scam wallets matching known crime syndicates based on 8-D behavioral sequence vector matching (91% match)."),
        ("⏱️ Live Mempool Monitoring", "Continuous mempool transaction ingestion stream with visual pulse beacons, pause/resume controls, and threat tags."),
        ("💼 Case Manager & Evidence Vault", "Multi-case workspace for investigating officers to manage FIR cases, record encrypted police notes, and export evidence archives."),
        ("📜 Legal Subpoena Dispatcher", "1-click generator and emergency API email dispatcher for Section 91 CrPC, US CLOUD Act § 2703(d), and MLAT freeze orders."),
        ("🌐 Public Wallet Safety Check", "Consumer pre-transaction scam screener providing instant SAFE, CAUTION, or ⛔ DO NOT SEND verdicts to prevent fraud before transfer."),
        ("🕵️ Fraud Network Map", "Cross-case crime syndicate graph correlating multiple independent victim complaints into an interconnected multi-case laundering nexus.")
    ]
    
    f_rows = [[Paragraph(f"<b>{title}</b>", ParagraphStyle('FT', fontName='Helvetica-Bold', fontSize=8, textColor=c_primary)), Paragraph(desc, body_style)] for title, desc in f_list]
    t_f = Table(f_rows, colWidths=[140, 360])
    t_f.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 3),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_f)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 4: DEEP-DIVE: FRAUD DNA™ & MIXER DEMASKING
    # =========================================================================
    story.append(Paragraph("4. Deep-Dive: Fraud DNA™ Behavioral Fingerprinting", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    dna_desc = (
        "<b>The Challenge with Static Blacklists:</b><br/>"
        "When a fraud syndicate launches a new campaign, they deploy fresh, unreported wallets (e.g. Wallet Z). "
        "Traditional databases flag Wallet Z as 'Clean' because no victim has reported it yet. CyberTrace overcomes this through <b>Fraud DNA™</b>.<br/><br/>"
        "<b>How Fraud DNA™ Works:</b><br/>"
        "CyberTrace computes an 8-dimensional behavioral vector fingerprint comparing the candidate wallet against indexed syndicate archetypes:<br/>"
        "&bull; <i>Transfer Cadence (94% weight):</i> Sub-45s automated bot script execution.<br/>"
        "&bull; <i>Peeling Ratio (92% weight):</i> Exact 80/20 tranche split matching Campaign #CYB-2048.<br/>"
        "&bull; <i>Hop Topology (96% weight):</i> 3-tier intermediary fan-out depth before consolidation.<br/>"
        "&bull; <i>Destination Gateway (91% weight):</i> Consolidation into Binance Hot Cluster 14.<br/>"
        "&bull; <i>Gas Lineage (86% weight):</i> Shared gas sponsorship via FixedFloat relayer.<br/><br/>"
        "<b>Result:</b> Immediate alert: <i>'🔴 Potential Unreported Fraud Wallet Detected — 91% Match with Campaign #CYB-2048 (\"Hydra-Peel\")'</i>."
    )
    t_dna = Table([[Paragraph(dna_desc, body_style)]], colWidths=[500])
    t_dna.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#fef2f2")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#fca5a5")),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_dna)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("5. Mixer &amp; Zero-Knowledge Obfuscation Demasking", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    mixer_desc = (
        "<b>De-anonymizing Tornado.Cash &amp; Privacy Protocols:</b><br/>"
        "CyberTrace employs deposit-withdrawal timing correlation and gas relayer lineage to break mixer anonymity sets:<br/>"
        "1. <i>Relayer Linkage:</i> Identifies that relayer <code>0xRelay99B</code> sponsored both the illicit 100 ETH deposit from suspect <code>0x742d...f44e</code> and the subsequent withdrawal to <code>0xCleanCash...11A9</code>.<br/>"
        "2. <i>Denomination Sizing:</i> Matches 100 ETH pool leaf index block brackets with withdrawal events.<br/>"
        "3. <i>Immediate Off-Ramp Correlation:</i> Withdrawn funds are traced within 32 minutes directly to OKX Exchange Hot Gateway #3.<br/>"
        "<b>Demasking Confidence:</b> 94.2% verified evidentiary score."
    )
    t_mix = Table([[Paragraph(mixer_desc, body_style)]], colWidths=[500])
    t_mix.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f5f3ff")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#c084fc")),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_mix)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 5: LEGAL ADMISSIBILITY & SUBPOENA GENERATION
    # =========================================================================
    story.append(Paragraph("6. Courtroom Admissibility &amp; Section 91 CrPC Subpoenas", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    story.append(Paragraph(
        "<b>Statutory Compliance under Indian Criminal Procedure:</b><br/>"
        "Cryptocurrency evidence generated by CyberTrace is structured for direct admissibility under Section 65B of the Indian Evidence Act and Section 91/102 of the Code of Criminal Procedure (CrPC). "
        "Every generated dossier includes cryptographic SHA-256 integrity stamps, full blockchain transaction IDs, UTC/IST timestamp mappings, and destination exchange nodal details.",
        body_style
    ))
    story.append(Spacer(1, 6))
    
    subpoena_sample = (
        "<b>SAMPLE AUTOMATED SECTION 91 CrPC LEGAL NOTICE:</b><br/>"
        "<b>NOTICE UNDER SECTION 91 OF CODE OF CRIMINAL PROCEDURE, 1973</b><br/>"
        "<b>To:</b> Nodal Law Enforcement Officer, Binance Services / WazirX India / CoinDCX<br/>"
        "<b>Subject:</b> Emergency Order to Freeze Suspect Cryptocurrency Assets in FIR #CYB-2026-001245<br/><br/>"
        "Whereas blockchain analytics generated by the CyberTrace Automated Forensics Engine (I4C) reveals that stolen proceeds of ₹20,000.00 "
        "were deposited into your Centralized Hot Deposit Gateway (0xExch...90A) on 23 Aug 2026, 05:40 PM IST via TXID: <code>0x4c2e5a7b9c1d3f6e8a0b2c4d6e8f0a2c4e6f3a</code>.<br/><br/>"
        "You are hereby commanded under Section 91 CrPC to immediately:<br/>"
        "1. Freeze the recipient account associated with deposit internal memo UID #8912401.<br/>"
        "2. Preserve all KYC documents, registration IP logs, linked bank accounts, and phone numbers.<br/>"
        "3. Furnish compliance confirmation within 24 hours to the Investigating Officer."
    )
    t_sub = Table([[Paragraph(subpoena_sample, body_style)]], colWidths=[500])
    t_sub.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_sub)
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("7. Step-by-Step Judges Live Demo Walkthrough", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    demo_steps = [
        [Paragraph("<b>Step 1</b>", body_style), Paragraph("<b>Enter Suspect Address:</b> Select preset pill for Case #1245 (<code>0xA1b2...9T0</code>).", body_style)],
        [Paragraph("<b>Step 2</b>", body_style), Paragraph("<b>Trigger Analysis:</b> Executes automated multi-hop blockchain crawl across EVM, Tron, and BTC.", body_style)],
        [Paragraph("<b>Step 3</b>", body_style), Paragraph("<b>Inspect Risk Score:</b> Review 87/100 High Risk AI gauge and 5-point evidence checklist.", body_style)],
        [Paragraph("<b>Step 4</b>", body_style), Paragraph("<b>Explore Fund-Flow &amp; Scrubber:</b> Play time-travel scrubber from T+00:00 to T+00:27.", body_style)],
        [Paragraph("<b>Step 5</b>", body_style), Paragraph("<b>Detect CEX Off-Ramp:</b> Identify Binance Hot Cluster 14 with 91% confidence.", body_style)],
        [Paragraph("<b>Step 6</b>", body_style), Paragraph("<b>Fraud DNA™ Zero-Day Test:</b> Click '🆕 Unreported Wallet Z' to trigger 91% match with Campaign #CYB-2048.", body_style)],
        [Paragraph("<b>Step 7</b>", body_style), Paragraph("<b>Export Legal Dossier:</b> Click 'Generate Dossier' to print court-ready Section 91 CrPC PDF.", body_style)]
    ]
    t_demo = Table(demo_steps, colWidths=[65, 435])
    t_demo.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_demo)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 6: ARCHITECTURE, DEPLOYMENT & QUICK ACCESS
    # =========================================================================
    story.append(Paragraph("8. Technical Architecture &amp; Deployment", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    story.append(Paragraph(
        "<b>Frontend:</b> Semantic HTML5, Vanilla JavaScript (ES6+), Vanilla CSS3 (Custom Glassmorphic Dark Design System).<br/>"
        "<b>Visualization:</b> Native Responsive SVG Engines, Dynamic Bezier Particle Flow Lines, Matrix Radars.<br/>"
        "<b>Zero Dependency Architecture:</b> Runs natively in any modern browser without heavy build steps, ensuring instant deployment on police intranet systems.",
        body_style
    ))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("9. Project Links &amp; Verification Resources", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    res_data = [
        [Paragraph("<b>GitHub Repository:</b>", body_style), Paragraph("<font color='#0066ff'><u>https://github.com/Hidayatulla268/CyberTrace</u></font>", body_style)],
        [Paragraph("<b>Live Website (GitHub Pages):</b>", body_style), Paragraph("<font color='#0066ff'><u>https://hidayatulla268.github.io/CyberTrace/</u></font>", body_style)],
        [Paragraph("<b>Documentation PDF:</b>", body_style), Paragraph("<font color='#0066ff'><u>CyberTrace_Platform_Guide.pdf</u></font>", body_style)],
        [Paragraph("<b>Primary Contact:</b>", body_style), Paragraph("Shaik Hidayatulla &bull; hidayatullashaik268@gmail.com", body_style)]
    ]
    t_res = Table(res_data, colWidths=[160, 340])
    t_res.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_res)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph(
        "<font size=7.5 color='#64748b'><i>CyberTrace is developed for the Smart India Hackathon 2026 (Problem Statement 26183) for the Indian Cyber Crime Coordination Centre (I4C), Ministry of Home Affairs, Government of India. All rights reserved.</i></font>",
        ParagraphStyle('EndNote', alignment=1)
    ))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Comprehensive 6-page Enterprise PDF generated: {output_path}")

if __name__ == '__main__':
    out_file = os.path.join(r"c:\Users\HP\OneDrive\Desktop\crypto", "CyberTrace_Platform_Guide.pdf")
    build_enterprise_pdf(out_file)
