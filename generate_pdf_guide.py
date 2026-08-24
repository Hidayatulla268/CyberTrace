"""
CyberTrace - Master Documentation & Comprehensive Platform Comparison PDF Generator
Generates an exhaustive, publication-grade manual featuring an in-depth Difference Table comparing CyberTrace with all major global forensic platforms.
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
        self.drawString(50, 11 * 72 - 36, "CYBERTRACE &bull; COMPREHENSIVE PLATFORM GUIDE &amp; GLOBAL DIFFERENCE MATRIX")
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
    c_dark = colors.HexColor("#0f172a")
    
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=27,
        textColor=c_dark
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=14.5,
        textColor=colors.HexColor("#475569")
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16.5,
        textColor=c_dark,
        spaceBefore=8,
        spaceAfter=3
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13.5,
        textColor=c_primary,
        spaceBefore=5,
        spaceAfter=2
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.8,
        textColor=colors.HexColor("#334155"),
        spaceAfter=3
    )

    tbl_hdr_style = ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10,
        textColor=colors.HexColor("#0f172a"),
        alignment=1
    )

    tbl_cell_style = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.4,
        leading=9.8,
        textColor=colors.HexColor("#334155")
    )

    tbl_bold_cell = ParagraphStyle(
        'TblBoldCell',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.4,
        leading=9.8,
        textColor=colors.HexColor("#0066ff")
    )
    
    story = []
    
    # =========================================================================
    # PAGE 1: COVER & EXECUTIVE OVERVIEW
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("🛡️ <b>CYBERTRACE</b>", ParagraphStyle('LogoText', fontName='Helvetica-Bold', fontSize=22, textColor=c_primary, leading=26)))
    story.append(Paragraph("Enterprise Crypto Forensics &amp; Comparative Platform Intelligence Manual", title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Smart India Hackathon 2026 &bull; Problem Statement PS-26183</b><br/>Indian Cyber Crime Coordination Centre (I4C) &bull; Ministry of Home Affairs, Government of India", subtitle_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=c_primary, spaceBefore=2, spaceAfter=10))
    
    meta_data = [
        [Paragraph("<b>Author / Lead:</b> Shaik Hidayatulla", body_style), Paragraph("<b>Global Benchmarks:</b> Chainalysis, TRM, Arkham, Elliptic", body_style)],
        [Paragraph("<b>Status:</b> Production Ready v2.0", body_style), Paragraph("<b>Target Focus:</b> 1930 Helpline &amp; I4C Police Officers", body_style)],
        [Paragraph("<b>GitHub Repo:</b> github.com/Hidayatulla268/CyberTrace", body_style), Paragraph("<b>Live App:</b> hidayatulla268.github.io/CyberTrace/", body_style)]
    ]
    t_meta = Table(meta_data, colWidths=[255, 255])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('PADDING', (0, 0), (-1, -1), 5),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))
    
    what_is_text = (
        "<b>What is CyberTrace in Simple Words?</b><br/>"
        "CyberTrace is an <b>Automated Crypto Forensics &amp; Anti-Fraud Intelligence Platform</b> built specifically for Law Enforcement Agencies (I4C, State Cyber Cells, 1930 Helpline). "
        "When a citizen reports losing money to a crypto scam (such as fake Telegram job scams, investment frauds, or ransomware), "
        "CyberTrace takes the suspect wallet address and in under 1 second: (1) Traces where the stolen money went hop-by-hop, "
        "(2) Discovers accomplice mule infrastructure, (3) Identifies which Centralized Exchange received the funds, "
        "(4) Matches the criminal syndicate's behavioral Fraud DNA™, and (5) Automatically generates court-admissible Section 91 CrPC freeze orders."
    )
    t_what = Table([[Paragraph(what_is_text, body_style)]], colWidths=[510])
    t_what.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#e0f2fe")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#38bdf8")),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_what)
    story.append(Spacer(1, 10))
    
    # Core USP Workflow Banner
    story.append(Paragraph("⭐ <b>THE 6-STEP MASTER FORENSIC WORKFLOW (USP)</b>", h2_style))
    usp_steps = [
        [
            Paragraph("<font color='#0066ff'><b>1. REPORT</b></font><br/><font size=6.5 color='#475569'>Victim Intake</font>", ParagraphStyle('U1', fontName='Helvetica-Bold', fontSize=7.5, alignment=1, leading=9)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=10, alignment=1)),
            Paragraph("<font color='#0066ff'><b>2. TRACE</b></font><br/><font size=6.5 color='#475569'>Stolen Funds</font>", ParagraphStyle('U2', fontName='Helvetica-Bold', fontSize=7.5, alignment=1, leading=9)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=10, alignment=1)),
            Paragraph("<font color='#0066ff'><b>3. CONNECT</b></font><br/><font size=6.5 color='#475569'>Hidden Wallets</font>", ParagraphStyle('U3', fontName='Helvetica-Bold', fontSize=7.5, alignment=1, leading=9)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=10, alignment=1)),
            Paragraph("<font color='#0066ff'><b>4. IDENTIFY</b></font><br/><font size=6.5 color='#475569'>Exchange CEX</font>", ParagraphStyle('U4', fontName='Helvetica-Bold', fontSize=7.5, alignment=1, leading=9)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=10, alignment=1)),
            Paragraph("<font color='#0066ff'><b>5. MONITOR</b></font><br/><font size=6.5 color='#475569'>Live Mempool</font>", ParagraphStyle('U5', fontName='Helvetica-Bold', fontSize=7.5, alignment=1, leading=9)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=10, alignment=1)),
            Paragraph("<font color='#0066ff'><b>6. PROVE</b></font><br/><font size=6.5 color='#475569'>I4C Dossier</font>", ParagraphStyle('U6', fontName='Helvetica-Bold', fontSize=7.5, alignment=1, leading=9))
        ]
    ]
    t_usp = Table(usp_steps, colWidths=[68, 14, 68, 14, 68, 14, 68, 14, 68, 14, 68])
    t_usp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_usp)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 2: THE COMPREHENSIVE DIFFERENCE TABLE
    # =========================================================================
    story.append(Paragraph("1. Comprehensive Platform Difference Matrix", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    story.append(Paragraph(
        "The following table provides a rigorous side-by-side technical and operational comparison between <b>CyberTrace</b> and the leading global blockchain analytics tools in the industry.",
        body_style
    ))
    story.append(Spacer(1, 4))
    
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
            Paragraph("<b>Multi-Hop Fund Flow Graph</b>", tbl_cell_style),
            Paragraph("Static nodes, manual layout", tbl_cell_style),
            Paragraph("Interactive 2D graph", tbl_cell_style),
            Paragraph("Entity link graph", tbl_cell_style),
            Paragraph("Node tree visualizer", tbl_cell_style),
            Paragraph("<b>Interactive SVG + Animated Particle Speed Flow</b>", tbl_bold_cell)
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
            Paragraph("<b>Citizen Safety Screener</b>", tbl_cell_style),
            Paragraph("No (Enterprise access only)", tbl_cell_style),
            Paragraph("No (Enterprise access only)", tbl_cell_style),
            Paragraph("No pre-tx safety verdict", tbl_cell_style),
            Paragraph("No (Enterprise access only)", tbl_cell_style),
            Paragraph("<b>Free 'Check Before You Send' Citizen Protection Tool</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Live Blockchain Web3 Mode</b>", tbl_cell_style),
            Paragraph("Proprietary API", tbl_cell_style),
            Paragraph("Proprietary API", tbl_cell_style),
            Paragraph("Proprietary API", tbl_cell_style),
            Paragraph("Proprietary API", tbl_cell_style),
            Paragraph("<b>Direct JSON-RPC Mainnet Queries (Real Balance &amp; Nonces)</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Cost &amp; Accessibility</b>", tbl_cell_style),
            Paragraph("$50,000+ per year", tbl_cell_style),
            Paragraph("$60,000+ per year", tbl_cell_style),
            Paragraph("Freemium API subscription", tbl_cell_style),
            Paragraph("$40,000+ per year", tbl_cell_style),
            Paragraph("<b>100% Free &amp; Open for Indian Police &amp; LEAs</b>", tbl_bold_cell)
        ],
        [
            Paragraph("<b>Deployment Barrier</b>", tbl_cell_style),
            Paragraph("Cloud enterprise login", tbl_cell_style),
            Paragraph("Cloud enterprise login", tbl_cell_style),
            Paragraph("Web account creation", tbl_cell_style),
            Paragraph("Cloud enterprise login", tbl_cell_style),
            Paragraph("<b>Zero dependency: runs in any browser, zero build setup</b>", tbl_bold_cell)
        ]
    ]
    t_diff = Table(diff_table_data, colWidths=[95, 83, 83, 83, 83, 83])
    t_diff.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 2.8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_diff)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 3: DETAILED FEATURES 1 TO 6 WITH PRACTICAL EXAMPLES
    # =========================================================================
    story.append(Paragraph("2. Detailed Feature Guide with Practical Examples (Part 1)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    f1_6 = [
        [
            Paragraph("<b>🔍 1. Smart Multi-Chain Wallet Scanner</b><br/>"
                      "<b>What it does:</b> Scans any wallet address (EVM, Tron, Bitcoin, Solana) and instantly displays total received funds, sent funds, transaction count, active dates, and live on-chain balances.<br/>"
                      "<i><b>Real-World Example:</b> An investigator enters suspect address <code>0xA1b2...9T0</code>. The system displays ₹8,42,000 received across 128 transactions, showing activity started on 12 Aug 2026 and last moved today at 05:42 PM.</i>", body_style)
        ],
        [
            Paragraph("<b>💰 2. Stolen Money Tracker (Tranche Following)</b><br/>"
                      "<b>What it does:</b> Instead of just looking at total volume, it locks onto a specific victim's deposit (e.g. ₹50,000) and follows that exact tranche hop-by-hop as the scammers split and launder it.<br/>"
                      "<i><b>Real-World Example:</b> Victim deposits ₹50,000. CyberTrace calculates: Hop 1 split ₹30k (60%) to Mule Wallet A and ₹20k (40%) to Binance. Hop 2 split ₹18k (36%) to WazirX and ₹12k (24%) to an intermediary. Offers 1-click CSV export of the full money trail.</i>", body_style)
        ],
        [
            Paragraph("<b>🕸️ 3. Animated Fund-Flow Graph</b><br/>"
                      "<b>What it does:</b> Visually diagrams the flow of money as an interactive flowchart: <code>Victim &rarr; Scammer Hub &rarr; Splitter Mules &rarr; Centralized Exchange</code> with animated particles showing the direction of speed.<br/>"
                      "<i><b>Real-World Example:</b> Instead of reading a confusing list of 100 transaction hashes, the police officer sees clear glowing boxes connected by arrows, showing exactly how funds moved from the victim's wallet to Binance Hot Cluster 14.</i>", body_style)
        ],
        [
            Paragraph("<b>🎯 4. Time-Travel Transaction Scrubber</b><br/>"
                      "<b>What it does:</b> An interactive playback bar on the Fund-Flow graph with Play, Pause, Step Back, and Speed (1x to 4x) controls that replays the crime chronologically from Hour 0 to Hour 24.<br/>"
                      "<i><b>Real-World Example:</b> Dragging the scrubber slider from 0% to 100% shows: at T+00:00 victim funds arrive; at T+00:25 the first split occurs; at T+00:27 funds hit the exchange deposit gateway, proving automated laundering in under 30 seconds.</i>", body_style)
        ],
        [
            Paragraph("<b>🏦 5. Exchange Finder (CEX Attribution)</b><br/>"
                      "<b>What it does:</b> Automatically detects whether stolen funds landed inside a centralized crypto exchange (such as Binance, WazirX, CoinDCX, KuCoin, or OKX) where KYC identity is stored.<br/>"
                      "<i><b>Real-World Example:</b> Analyzes the final recipient address and confirms with <b>91% confidence</b> that the address belongs to <code>Binance Hot Cluster 14</code>, enabling police to know exactly which company to subpoena.</i>", body_style)
        ],
        [
            Paragraph("<b>🔗 6. Hidden Wallet &amp; Accomplice Detector</b><br/>"
                      "<b>What it does:</b> Uncovers accomplice wallets that never directly touched the victim, including Gas Sponsors (who paid transaction fees), Co-Spenders, and Peeling Splitters.<br/>"
                      "<i><b>Real-World Example:</b> Discovers that wallet <code>0xFeef...119A</code> funded gas fees for 12 different scammer hubs via FixedFloat, exposing the underlying bot infrastructure.</i>", body_style)
        ]
    ]
    t_f1_6 = Table(f1_6, colWidths=[510])
    t_f1_6.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 4.2),
    ]))
    story.append(t_f1_6)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 4: DETAILED FEATURES 7 TO 12 WITH PRACTICAL EXAMPLES
    # =========================================================================
    story.append(Paragraph("3. Detailed Feature Guide with Practical Examples (Part 2)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    f7_12 = [
        [
            Paragraph("<b>🚨 7. Heuristic AI Risk Score Gauge (0–100)</b><br/>"
                      "<b>What it does:</b> Calculates a dynamic risk score from 0 (Safe) to 100 (Critical Risk) with clear bullet-pointed reasons explaining why the wallet is dangerous.<br/>"
                      "<i><b>Real-World Example:</b> Suspect wallet gets an <b>87/100 HIGH RISK</b> score because: (1) Rapid peeling chain detected, (2) Funds split across 3 wallets in 12 mins, (3) Consolidated into Binance sweep gateway, (4) Reported by multiple victims on 1930 portal.</i>", body_style)
        ],
        [
            Paragraph("<b>🧠 8. Fraud Pattern Detection Engine</b><br/>"
                      "<b>What it does:</b> Detects automated laundering signatures including: Peeling Chains (shaving off small tranches), Rapid Transfers (<45s cadence), Fan-Out (splitting to multiple mules), and Fan-In (re-gathering funds).<br/>"
                      "<i><b>Real-World Example:</b> Detects that funds were transferred across 3 hops in 42 seconds, proving the scam is operated by an automated bot network rather than a human user.</i>", body_style)
        ],
        [
            Paragraph("<b>🧬 9. Fraud DNA™ Syndicate Attribution (Zero-Day Detection)</b><br/>"
                      "<b>What it does:</b> Detects new, unknown scam wallets even if nobody has ever reported them before, by matching their behavioral sequence fingerprint against known crime syndicate playbooks.<br/>"
                      "<i><b>Real-World Example:</b> Scammers deploy brand new Wallet Z. CyberTrace calculates an 8-dimensional vector (timing, peeling ratio, exchange gateway) and alerts: <b>'🔴 91% Match to Campaign #CYB-2048 (Hydra-Peel Telegram Scam Syndicate)'</b>.</i>", body_style)
        ],
        [
            Paragraph("<b>🌉 10. Cross-Chain Bridge &amp; Hop Tracker (TRM Labs Style)</b><br/>"
                      "<b>What it does:</b> Follows funds when scammers try to evade police by hopping across blockchains (e.g. from Ethereum to Tron, BSC, Bitcoin, or Solana) using bridge protocols like Across and FixedFloat.<br/>"
                      "<i><b>Real-World Example:</b> Scammer deposits ERC-20 USDT on Ethereum, bridges via Across Protocol to TRC-20 USDT on Tron, and off-ramps to Binance BSC. CyberTrace unifies all chains into one continuous forensic flow.</i>", body_style)
        ],
        [
            Paragraph("<b>🏷️ 11. 100k+ Entity &amp; Deanonymization Directory (Arkham Style)</b><br/>"
                      "<b>What it does:</b> Searchable database of 100,000+ indexed real-world labels: Centralized Exchanges, Lazarus Group APT addresses, LockBit Ransomware vaults, and Darknet marketplaces.<br/>"
                      "<i><b>Real-World Example:</b> Search for 'Lazarus' or 'Binance' to immediately see associated hotwallet clusters, historical stolen volume (₹4,800 Cr), and click 'Trace' to load full transaction ledgers.</i>", body_style)
        ],
        [
            Paragraph("<b>🌪️ 12. Mixer Demasking Engine (Elliptic Style)</b><br/>"
                      "<b>What it does:</b> De-anonymizes privacy pools like Tornado.Cash by identifying common relayer gas dispatchers (e.g. 0xRelay99B) and matching deposit-withdrawal timing brackets.<br/>"
                      "<i><b>Real-World Example:</b> Suspect deposits 100 ETH into Tornado Cash. CyberTrace links the gas relayer to the withdrawal wallet 32 minutes later, shrinking the anonymity set from 10,000 to a single target with 94.2% confidence.</i>", body_style)
        ]
    ]
    t_f7_12 = Table(f7_12, colWidths=[510])
    t_f7_12.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 4.2),
    ]))
    story.append(t_f7_12)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 5: DETAILED FEATURES 13 TO 18 WITH PRACTICAL EXAMPLES
    # =========================================================================
    story.append(Paragraph("4. Detailed Feature Guide with Practical Examples (Part 3)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    f13_18 = [
        [
            Paragraph("<b>🛡️ 13. Global Sanctions &amp; OFAC Screener</b><br/>"
                      "<b>What it does:</b> Real-time anti-money laundering (AML) screening checking whether any suspect wallet is listed on US OFAC SDN, UN Sanctions, EU Blacklists, or FIU-IND registries.<br/>"
                      "<i><b>Real-World Example:</b> Scanning a ransomware address instantly displays a red badge: <b>'OFAC SDN Sanctioned — DPRK State Sponsored Threat'</b>, alerting police to involve international agencies.</i>", body_style)
        ],
        [
            Paragraph("<b>⏱️ 14. Live Mempool Monitoring Stream</b><br/>"
                      "<b>What it does:</b> Live blockchain feed that watches flagged wallets in real-time and alerts investigators with visual pulse beacons the exact second new transactions are broadcast.<br/>"
                      "<i><b>Real-World Example:</b> While an officer is investigating Case #1245, a new ₹80,000 transaction is broadcast to the mempool. The live feed lights up green: 'Live Event: ₹80,000 moved to Binance Hot 14', enabling instant action.</i>", body_style)
        ],
        [
            Paragraph("<b>💼 15. Investigator Case Workspace &amp; Evidence Vault</b><br/>"
                      "<b>What it does:</b> Multi-case organizer where police officers can manage multiple FIRs, assign junior officers, write encrypted case notes, and maintain an audit log of evidence.<br/>"
                      "<i><b>Real-World Example:</b> Officer records notes: 'Requested Binance KYC for UID #8912401 on 24 Aug. Bank account frozen via 1930 portal.' Notes are encrypted and stored in the local vault.</i>", body_style)
        ],
        [
            Paragraph("<b>📜 16. Multi-Jurisdictional Legal Subpoena Dispatcher</b><br/>"
                      "<b>What it does:</b> 1-click generator and emergency API dispatcher that formats complete legal notices under Section 91 CrPC (India), US CLOUD Act § 2703(d), and MLAT freeze orders.<br/>"
                      "<i><b>Real-World Example:</b> Automatically generates a formal Section 91 CrPC notice pre-filled with the transaction hash, deposit amount (₹20,000), timestamp, and sends it directly to Binance's Nodal Officer.</i>", body_style)
        ],
        [
            Paragraph("<b>🌐 17. Public Wallet Safety Check ('Check Before You Send')</b><br/>"
                      "<b>What it does:</b> A public consumer protection tool where citizens can paste any wallet address before paying someone online to verify if it is safe or a reported scam.<br/>"
                      "<i><b>Real-World Example:</b> A student is asked to send ₹10,000 to a crypto wallet for a 'Telegram job'. They check the address on CyberTrace, which displays: <b>'⛔ DO NOT SEND — 91% Match with Known Fraud Syndicate'</b>, preventing the loss before it happens.</i>", body_style)
        ],
        [
            Paragraph("<b>⚡ 18. Real-Time On-Chain RPC Querying (Live Web3 Mode)</b><br/>"
                      "<b>What it does:</b> Directly queries live Ethereum and BSC mainnet RPCs in real-time, fetching real on-chain ETH balances, nonces, and transaction counts for any live wallet.<br/>"
                      "<i><b>Real-World Example:</b> Entering Vitalik Buterin's address (<code>0xd8dA...6045</code>) queries Ethereum mainnet and displays real live balance: <b>6.6410 ETH (₹18,26,275)</b> across 5,956 live transactions.</i>", body_style)
        ]
    ]
    t_f13_18 = Table(f13_18, colWidths=[510])
    t_f13_18.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 4.2),
    ]))
    story.append(t_f13_18)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 6: LIVE DEMO TOUR, ARCHITECTURE & RESOURCE LINKS
    # =========================================================================
    story.append(Paragraph("5. Step-by-Step 7-Stage Guided Live Demo Tour", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    demo_steps = [
        [Paragraph("<b>Step 1: Enter Address</b>", body_style), Paragraph("Click the preset pill <code>Task-Based Telegram Scam (₹50k)</code> to load suspect address <code>0xA1b2...9T0</code>.", body_style)],
        [Paragraph("<b>Step 2: Trigger Analysis</b>", body_style), Paragraph("Click <b>Analyze</b>. The automated engine scans transactions, queries balances, and identifies risk patterns.", body_style)],
        [Paragraph("<b>Step 3: Risk Score</b>", body_style), Paragraph("Observe the <b>87/100 High Risk</b> AI gauge and the 5-point evidence checklist.", body_style)],
        [Paragraph("<b>Step 4: Flow Graph</b>", body_style), Paragraph("Play the <b>Time-Travel Scrubber</b> to see money move chronologically from Victim to Binance.", body_style)],
        [Paragraph("<b>Step 5: Exchange Detection</b>", body_style), Paragraph("See <b>Binance Hot Cluster 14</b> detected with 91% confidence.", body_style)],
        [Paragraph("<b>Step 6: Fraud DNA™ Zero-Day</b>", body_style), Paragraph("Click <code>🆕 Unreported Wallet Z</code> to see zero-day detection matching Campaign #CYB-2048 at 91%.", body_style)],
        [Paragraph("<b>Step 7: Generate Dossier</b>", body_style), Paragraph("Click <b>Download Dossier</b> to export the official Section 91 CrPC court evidence PDF.", body_style)]
    ]
    t_demo = Table(demo_steps, colWidths=[120, 390])
    t_demo.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 3),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_demo)
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("6. Quick Reference Links &amp; Contacts", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    res_data = [
        [Paragraph("<b>Live Platform (GitHub Pages):</b>", body_style), Paragraph("<font color='#0066ff'><u>https://hidayatulla268.github.io/CyberTrace/</u></font>", body_style)],
        [Paragraph("<b>GitHub Repository:</b>", body_style), Paragraph("<font color='#0066ff'><u>https://github.com/Hidayatulla268/CyberTrace</u></font>", body_style)],
        [Paragraph("<b>Documentation PDF File:</b>", body_style), Paragraph("<font color='#0066ff'><u>CyberTrace_Platform_Guide.pdf</u></font>", body_style)],
        [Paragraph("<b>Project Lead &amp; Developer:</b>", body_style), Paragraph("Shaik Hidayatulla &bull; hidayatullashaik268@gmail.com", body_style)]
    ]
    t_res = Table(res_data, colWidths=[170, 340])
    t_res.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 4.5),
    ]))
    story.append(t_res)
    story.append(Spacer(1, 10))
    
    story.append(Paragraph(
        "<font size=7 color='#64748b'><i>CyberTrace is developed for the Smart India Hackathon 2026 (Problem Statement PS-26183) in collaboration with the Indian Cyber Crime Coordination Centre (I4C), Ministry of Home Affairs, Government of India. All rights reserved.</i></font>",
        ParagraphStyle('EndNote', alignment=1)
    ))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Master Comprehensive PDF Guide with Difference Table generated: {output_path}")

if __name__ == '__main__':
    out_file = os.path.join(r"c:\Users\HP\OneDrive\Desktop\crypto", "CyberTrace_Platform_Guide.pdf")
    build_comprehensive_pdf(out_file)
