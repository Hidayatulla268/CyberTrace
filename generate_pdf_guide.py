"""
CyberTrace - Master Documentation & Comprehensive Platform Guide PDF Generator
Generates a multi-page publication-grade manual featuring:
- Dual Forensics Engine Architecture (Crypto Blockchain & UPI Banking Rails)
- 5 Crypto Crime & 5 Banking Presets
- Real-World Geographic Cartographic Map
- Global Difference Matrix & Production Architecture Roadmap
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
        self.drawString(50, 11 * 72 - 36, "CYBERTRACE &bull; ENTERPRISE CRYPTO &amp; UPI BANKING FORENSICS PLATFORM")
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
        leading=25,
        textColor=c_dark
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#475569")
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=16,
        textColor=c_dark,
        spaceBefore=7,
        spaceAfter=3
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=c_primary,
        spaceBefore=4,
        spaceAfter=2
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor("#334155"),
        spaceAfter=3
    )

    tbl_hdr_style = ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#0f172a"),
        alignment=1
    )

    tbl_cell_style = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor("#334155")
    )

    tbl_bold_cell = ParagraphStyle(
        'TblBoldCell',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor("#0066ff")
    )
    
    story = []
    
    # =========================================================================
    # PAGE 1: COVER & EXECUTIVE OVERVIEW
    # =========================================================================
    story.append(Spacer(1, 8))
    story.append(Paragraph("🛡️ <b>CYBERTRACE</b>", ParagraphStyle('LogoText', fontName='Helvetica-Bold', fontSize=22, textColor=c_primary, leading=26)))
    story.append(Paragraph("Enterprise Crypto &amp; UPI Banking Forensics Platform Manual", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Smart India Hackathon 2026 &bull; Problem Statement PS-26183</b><br/>Indian Cyber Crime Coordination Centre (I4C) &bull; Ministry of Home Affairs, Government of India", subtitle_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=2, color=c_primary, spaceBefore=2, spaceAfter=8))
    
    meta_data = [
        [Paragraph("<b>Author / Lead:</b> Shaik Hidayatulla", body_style), Paragraph("<b>Global Benchmarks:</b> Chainalysis, TRM Labs, Arkham, Elliptic", body_style)],
        [Paragraph("<b>Status:</b> Production Ready v7.4", body_style), Paragraph("<b>Target Focus:</b> 1930 Helpline &amp; I4C Police Officers", body_style)],
        [Paragraph("<b>GitHub Repo:</b> github.com/Hidayatulla268/CyberTrace", body_style), Paragraph("<b>Live App:</b> hidayatulla268.github.io/CyberTrace/", body_style)]
    ]
    t_meta = Table(meta_data, colWidths=[255, 255])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('PADDING', (0, 0), (-1, -1), 4.5),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))
    
    what_is_text = (
        "<b>Executive Overview &amp; Dual Engine Architecture:</b><br/>"
        "CyberTrace is an <b>Automated Forensics &amp; Financial Crime Intelligence Platform</b> developed for Law Enforcement Agencies (I4C, State Cyber Cells, 1930 National Helpline). "
        "It solves the critical problem of multi-rail cyber laundering by providing dual specialized forensic workspaces:<br/>"
        "&bull; <b>Mode 1 (₿ Crypto Blockchain Engine):</b> Traces multi-chain illicit transactions (EVM, Bitcoin, Tron TRC-20, Solana), follows peeling tranches, uncovers mixer gas relayers, visualizes money flows on an authentic geographic vector map, and drafts Section 91 CrPC exchange subpoenas.<br/>"
        "&bull; <b>Mode 2 (📱 UPI &amp; Core Banking Engine):</b> Performs NPCI VPA lookups, maps multi-tier bank mule accounts, calculates retrievable balances before ATM sweeps, matches NCRP 1930 complaint patterns, and accesses 42+ Indian Bank Nodal Officer contacts."
    )
    t_what = Table([[Paragraph(what_is_text, body_style)]], colWidths=[510])
    t_what.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#e0f2fe")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#38bdf8")),
        ('PADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(t_what)
    story.append(Spacer(1, 8))
    
    # Core USP Workflow Banner
    story.append(Paragraph("⭐ <b>6-STEP MASTER FORENSIC PIPELINE (USP)</b>", h2_style))
    usp_steps = [
        [
            Paragraph("<font color='#0066ff'><b>1. REPORT</b></font><br/><font size=6 color='#475569'>Victim Intake</font>", ParagraphStyle('U1', fontName='Helvetica-Bold', fontSize=7, alignment=1, leading=8.5)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=9, alignment=1)),
            Paragraph("<font color='#0066ff'><b>2. TRACE</b></font><br/><font size=6 color='#475569'>Stolen Funds</font>", ParagraphStyle('U2', fontName='Helvetica-Bold', fontSize=7, alignment=1, leading=8.5)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=9, alignment=1)),
            Paragraph("<font color='#0066ff'><b>3. CONNECT</b></font><br/><font size=6 color='#475569'>Hidden Mules</font>", ParagraphStyle('U3', fontName='Helvetica-Bold', fontSize=7, alignment=1, leading=8.5)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=9, alignment=1)),
            Paragraph("<font color='#0066ff'><b>4. IDENTIFY</b></font><br/><font size=6 color='#475569'>CEX &amp; Banks</font>", ParagraphStyle('U4', fontName='Helvetica-Bold', fontSize=7, alignment=1, leading=8.5)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=9, alignment=1)),
            Paragraph("<font color='#0066ff'><b>5. MONITOR</b></font><br/><font size=6 color='#475569'>Live Gateway</font>", ParagraphStyle('U5', fontName='Helvetica-Bold', fontSize=7, alignment=1, leading=8.5)),
            Paragraph("&rarr;", ParagraphStyle('UA', fontSize=9, alignment=1)),
            Paragraph("<font color='#0066ff'><b>6. PROVE</b></font><br/><font size=6 color='#475569'>Sec 91 Dossier</font>", ParagraphStyle('U6', fontName='Helvetica-Bold', fontSize=7, alignment=1, leading=8.5))
        ]
    ]
    t_usp = Table(usp_steps, colWidths=[68, 14, 68, 14, 68, 14, 68, 14, 68, 14, 68])
    t_usp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 3.5),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_usp)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 2: COMPREHENSIVE DIFFERENCE TABLE
    # =========================================================================
    story.append(Paragraph("1. Global Platform Difference Matrix", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    story.append(Paragraph(
        "Side-by-side technical and operational comparison between <b>CyberTrace</b> and major commercial blockchain analytics platforms:",
        body_style
    ))
    story.append(Spacer(1, 3))
    
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
        ('PADDING', (0, 0), (-1, -1), 2.5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_diff)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 3: 5 CRYPTO PRESETS & CARTOGRAPHIC MAP
    # =========================================================================
    story.append(Paragraph("2. Mode 1: ₿ Crypto Blockchain Engine &amp; Realistic Presets", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    crypto_presets = [
        [
            Paragraph("<b>⚡ Preset 1: Lazarus Group APT-38 Exploit (<code>0x098B...f96</code>)</b><br/>"
                      "<b>Crime Modus Operandi:</b> State-sponsored multi-sig smart contract exploit. Scammers routed ₹18.5 Cr ($2.2M) through Tornado Cash 100 ETH mixer pools before off-ramping to Binance.<br/>"
                      "<b>Forensic Profile:</b> 98% Critical Risk &bull; OFAC Sanctioned &bull; Attribution: Tornado.Cash Mixer &bull; Binance Off-Ramp Gateway.", body_style)
        ],
        [
            Paragraph("<b>💼 Preset 2: Telegram Task Job Scam (<code>0xA1b2...9T0</code>)</b><br/>"
                      "<b>Crime Modus Operandi:</b> High-cadence peeling chain scam. Split ₹84,500 across 3 intermediate hops in under 45 seconds to evade detection before sweeping to an Indian exchange.<br/>"
                      "<b>Forensic Profile:</b> 91% High Risk &bull; Campaign #CYB-2048 (Hydra-Peel) &bull; Attribution: WazirX India Gateway Hot 02.", body_style)
        ],
        [
            Paragraph("<b>👮 Preset 3: Digital Arrest &amp; Video Sextortion (<code>0x742d...44e</code>)</b><br/>"
                      "<b>Crime Modus Operandi:</b> Fake police video call extortion using permit2 token drainers to siphon victim crypto directly into Dubai OTC off-ramps.<br/>"
                      "<b>Forensic Profile:</b> 96% Critical Risk &bull; Active NCRP FIRs &bull; Attribution: CoinDCX Off-Ramp Hub &bull; Dubai OTC Cashout Desk.", body_style)
        ],
        [
            Paragraph("<b>📈 Preset 4: Pig Butchering Arbitrage Scam (<code>0x8920...3e7</code>)</b><br/>"
                      "<b>Crime Modus Operandi:</b> Fake liquidity mining platform promising 400% returns. Siphoned ₹1.45 Cr into multi-sig consolidation vaults.<br/>"
                      "<b>Forensic Profile:</b> 88% High Risk &bull; Campaign #CYB-1084 (Golden-Boar) &bull; Attribution: OKX &amp; KuCoin Multi-Sig Vault.", body_style)
        ],
        [
            Paragraph("<b>🏛️ Preset 5: Binance Official Hot Wallet 14 (<code>0x28C6...1d60</code>)</b><br/>"
                      "<b>Benchmark Control:</b> Official verified institutional exchange wallet used to validate false-positive rates.<br/>"
                      "<b>Forensic Profile:</b> 12% Verified Safe Control &bull; Institutional Hot Wallet &bull; 0 NCRP Complaints.", body_style)
        ],
        [
            Paragraph("<b>🗺️ Real-World Vector Cartographic Map</b><br/>"
                      "High-definition SVG vector landmass paths depicting real city coordinates (Mumbai, Delhi, Bengaluru, Hyderabad, Kolkata, Surat, Dubai, Singapore, Hong Kong, Bangkok, Zurich, London, Seychelles) with animated radar scan rings and curved flight trajectories.", body_style)
        ]
    ]
    t_cp = Table(crypto_presets, colWidths=[510])
    t_cp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 3.8),
    ]))
    story.append(t_cp)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 4: 5 UPI BANKING PRESETS & BANKING RAILS
    # =========================================================================
    story.append(Paragraph("3. Mode 2: 📱 UPI &amp; Core Banking Forensics Rails", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    bank_presets = [
        [
            Paragraph("<b>💼 Preset 1: Telegram Job Scam VPA (<code>daily.payout@oksbi</code>)</b><br/>"
                      "<b>Core Bank &amp; Branch:</b> State Bank of India &bull; Andheri East, Mumbai (`SBIN0001245`) &bull; A/C: `3819****4812`<br/>"
                      "<b>Forensic Data:</b> ₹84,500 Inflow &bull; 14 NCRP Complaints &bull; SIM Swapped in Surat, Gujarat &bull; Retrievable: ₹30,420 (SBI Surat Mule).", body_style)
        ],
        [
            Paragraph("<b>👮 Preset 2: Digital Arrest Fake CBI Fund (<code>cbi.investigation.fund@okaxis</code>)</b><br/>"
                      "<b>Core Bank &amp; Branch:</b> Axis Bank &bull; Connaught Place, New Delhi (`UTIB0000188`) &bull; A/C: `9230****9104`<br/>"
                      "<b>Forensic Data:</b> ₹1,50,000 Inflow &bull; 22 NCRP Complaints &bull; IP Routed via Cambodia Proxy &bull; Retrievable: ₹54,000.", body_style)
        ],
        [
            Paragraph("<b>⚡ Preset 3: Phishing QR Code Scam (<code>quick.pay24@ybl</code>)</b><br/>"
                      "<b>Core Bank &amp; Branch:</b> Yes Bank Limited &bull; Indiranagar, Bengaluru (`YESB0000412`) &bull; A/C: `0041****1984`<br/>"
                      "<b>Forensic Data:</b> ₹25,000 Inflow &bull; 8 NCRP Complaints &bull; Jamtara Jharkhand Ring &bull; Retrievable: ₹9,000.", body_style)
        ],
        [
            Paragraph("<b>💡 Preset 4: Fake Electricity Bill APK (<code>UTR-20260825-991240</code>)</b><br/>"
                      "<b>Core Bank &amp; Branch:</b> Punjab National Bank / HDFC &bull; Salt Lake, Kolkata (`PUNB0142800`) &bull; A/C: `1428****5520`<br/>"
                      "<b>Forensic Data:</b> ₹42,000 Inflow &bull; 6 NCRP Complaints &bull; Remote Access SMS Scraper &bull; Retrievable: ₹15,120.", body_style)
        ],
        [
            Paragraph("<b>🏏 Preset 5: Offshore IPL Betting Gateway (<code>vip.gaming.deposit@paytm</code>)</b><br/>"
                      "<b>Core Bank &amp; Branch:</b> Paytm Payments Bank &bull; Sector 62, Noida (`PYTM0123456`) &bull; A/C: `9102****7712`<br/>"
                      "<b>Forensic Data:</b> ₹2,10,000 Inflow &bull; 31 NCRP Complaints &bull; Dubai P2P Merchant Hub &bull; Retrievable: ₹75,600.", body_style)
        ],
        [
            Paragraph("<b>📜 Automated Section 91 CrPC Bank Freezing Order</b><br/>"
                      "Generates court-admissible legal orders with IFSC, Account Number, Transaction UTR, NCRP Complaint ID, and Police Stamp, ready for 1-click dispatch to Bank Nodal Desks.", body_style)
        ]
    ]
    t_bp = Table(bank_presets, colWidths=[510])
    t_bp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 3.8),
    ]))
    story.append(t_bp)
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 5: PRODUCTION ARCHITECTURE ROADMAP & SECURITY
    # =========================================================================
    story.append(Paragraph("4. Production Architecture &amp; Deployment Roadmap", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
    prod_info = (
        "<b>Enterprise Deployment Architecture (Law Enforcement Scale):</b><br/>"
        "&bull; <b>Backend API Gateway:</b> Node.js (Fastify/Express) or Python (FastAPI) acting as a secure proxy to protect private Pro API keys (Alchemy, Etherscan Pro, TronGrid, Moralis).<br/>"
        "&bull; <b>High-Speed Caching Layer:</b> Redis in-memory cache to store indexed multi-hop graph nodes and exchange cluster heuristics with sub-10ms response times.<br/>"
        "&bull; <b>Indian Banking Rails Integration:</b> RBI-regulated Account Aggregator (AA) framework (Setu, Anumati) and CKYC registry for automated bank statement ingestion.<br/>"
        "&bull; <b>Immutable Evidence Vault:</b> PostgreSQL database with PostGIS for spatial mapping and AWS S3 / Cloudflare R2 for SHA-256 cryptographically sealed court dossiers.<br/>"
        "&bull; <b>Authentication &amp; RBAC:</b> Multi-Factor Authentication (OTP/TOTP) and Role-Based Access Control for Police Officers, Cyber Cell Leads, and Nodal Officers."
    )
    t_prod = Table([[Paragraph(prod_info, body_style)]], colWidths=[510])
    t_prod.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f0fdf4")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_prod)
    story.append(Spacer(1, 6))

    story.append(Paragraph("5. Enterprise Security Layer &amp; Verification Resources", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=5))
    
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
        ('PADDING', (0, 0), (-1, -1), 4.5),
    ]))
    story.append(t_res)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph(
        "<font size=7 color='#64748b'><i>CyberTrace is developed for the Smart India Hackathon 2026 (Problem Statement PS-26183) in collaboration with the Indian Cyber Crime Coordination Centre (I4C), Ministry of Home Affairs, Government of India. All rights reserved.</i></font>",
        ParagraphStyle('EndNote', alignment=1)
    ))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Master Comprehensive PDF Guide generated: {output_path}")

if __name__ == '__main__':
    out_file = os.path.join(r"c:\Users\HP\OneDrive\Desktop\crypto", "CyberTrace_Platform_Guide.pdf")
    build_comprehensive_pdf(out_file)

