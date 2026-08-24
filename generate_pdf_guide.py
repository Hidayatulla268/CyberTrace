"""
CyberTrace - PDF Documentation Generator
Creates an enterprise-grade publication-quality PDF guide for CyberTrace (SIH 2026 PS-26183).
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
            return
        
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header
        self.drawString(54, 11 * 72 - 36, "CYBERTRACE &bull; CRYPTO FORENSICS INTELLIGENCE PLATFORM (SIH 2026 PS-26183)")
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
    
    c_primary = colors.HexColor("#0066ff")
    
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=colors.HexColor("#0f172a")
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#475569")
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=12,
        spaceAfter=5
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=c_primary,
        spaceBefore=8,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor("#334155"),
        spaceAfter=5
    )
    
    story = []
    
    # ==========================================
    # COVER PAGE
    # ==========================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("🛡️ <b>CYBERTRACE</b>", ParagraphStyle('LogoText', fontName='Helvetica-Bold', fontSize=22, textColor=c_primary, leading=26)))
    story.append(Paragraph("Enterprise Crypto Forensics &amp; Real-Time Blockchain Analytics Platform", title_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Smart India Hackathon 2026 &bull; Problem Statement PS-26183</b><br/>Indian Cyber Crime Coordination Centre (I4C) &bull; Ministry of Home Affairs, Government of India", subtitle_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=2, color=c_primary, spaceBefore=4, spaceAfter=12))
    
    meta_data = [
        [Paragraph("<b>Platform:</b> CyberTrace Enterprise Engine", body_style), Paragraph("<b>Global Benchmarks:</b> Chainalysis, TRM Labs, Arkham", body_style)],
        [Paragraph("<b>Author / Lead:</b> Shaik Hidayatulla", body_style), Paragraph("<b>Status:</b> Production Ready v2.0", body_style)],
        [Paragraph("<b>Repository:</b> github.com/Hidayatulla268/CyberTrace", body_style), Paragraph("<b>Live Demo:</b> hidayatulla268.github.io/CyberTrace/", body_style)]
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
    
    # ==========================================
    # SECTION 1: MASTER ENTERPRISE FEATURE MATRIX
    # ==========================================
    story.append(Paragraph("1. Enterprise Feature Matrix &amp; Global Comparison", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    features_data = [
        [Paragraph("<b>Feature &amp; Capability</b>", body_style), Paragraph("<b>Global Benchmark</b>", body_style), Paragraph("<b>CyberTrace Implementation</b>", body_style)],
        [Paragraph("🔍 Smart Multi-Chain Scanner", body_style), Paragraph("Etherscan / Blockchair", body_style), Paragraph("Multi-token balances (USDT, ETH, BTC, TRX, INR), ledgers &amp; address tagging.", body_style)],
        [Paragraph("💰 Stolen Money Tranche Tracker", body_style), Paragraph("Chainalysis Reactor", body_style), Paragraph("Hop-by-hop tranche tracker with retention percentages &amp; CSV export.", body_style)],
        [Paragraph("🕸️ Animated Fund-Flow Graph", body_style), Paragraph("MetaSleuth / Breadcrumbs", body_style), Paragraph("Interactive SVG flow canvas with particle animation, pan/zoom &amp; node popovers.", body_style)],
        [Paragraph("🎯 Time-Travel Playback Scrubber", body_style), Paragraph("Breadcrumbs / MetaSleuth", body_style), Paragraph("Play/pause scrubber animating transactions chronologically (Hour 0 to Hour 24).", body_style)],
        [Paragraph("🌉 Cross-Chain Bridge Tracker", body_style), Paragraph("TRM Labs Forensics", body_style), Paragraph("Tracks hops across Ethereum, Tron (TRC-20), BSC, Bitcoin via Across &amp; FixedFloat.", body_style)],
        [Paragraph("🏷️ 100k+ Entity Directory", body_style), Paragraph("Arkham Intelligence", body_style), Paragraph("Deanonymization database: CEXs, Lazarus Group, Tornado Cash, Darknet markets.", body_style)],
        [Paragraph("🌪️ Mixer Demasking Engine", body_style), Paragraph("Elliptic Investigator", body_style), Paragraph("Tornado.Cash 10/100 ETH deposit-withdrawal matching via gas relayer lineage.", body_style)],
        [Paragraph("🛡️ OFAC Sanctions Screener", body_style), Paragraph("Chainalysis KYT", body_style), Paragraph("Real-time compliance checks against US OFAC SDN, EU Sanctions &amp; FIU-IND alerts.", body_style)],
        [Paragraph("🧬 Fraud DNA™ Syndicate Matcher", body_style), Paragraph("Proprietary Innovation", body_style), Paragraph("Detects zero-day unreported wallets via 8-D behavioral sequence vector matching.", body_style)],
        [Paragraph("⏱️ Live Mempool Watchlist", body_style), Paragraph("SlowMist MistTrack", body_style), Paragraph("Live mempool ingestion stream with visual pulses and automated threat flags.", body_style)],
        [Paragraph("💼 Case Manager &amp; Evidence Vault", body_style), Paragraph("Chainalysis Case Manager", body_style), Paragraph("Multi-case workspace: assign police officers, add encrypted case notes &amp; export.", body_style)],
        [Paragraph("📜 Subpoena Dispatcher", body_style), Paragraph("I4C Law Enforcement", body_style), Paragraph("1-click Section 91 CrPC, US CLOUD Act, and MLAT freeze orders with API dispatch.", body_style)]
    ]
    t_feat = Table(features_data, colWidths=[140, 110, 250])
    t_feat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_feat)
    story.append(PageBreak())
    
    # ==========================================
    # SECTION 2: FRAUD DNA™ & MIXER DEMASKING
    # ==========================================
    story.append(Paragraph("2. Deep-Dive: Fraud DNA™ &amp; Zero-Knowledge Demasking", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    dna_desc = (
        "<b>Fraud DNA™ (Zero-Day Detection):</b><br/>"
        "Traditional tools only flag known addresses. Fraud DNA™ computes an 8-dimensional behavioral vector "
        "(Transfer Cadence, Peeling Ratio, Hop Depth, Tranche Size, CEX Gateway, Gas Sponsorship). "
        "When an unreported wallet appears, CyberTrace detects: <i>'🔴 Potential Unreported Fraud Wallet Detected — 91% match with Campaign #CYB-2048'</i>.<br/><br/>"
        "<b>Mixer &amp; Obfuscation Demasking:</b><br/>"
        "De-anonymizes privacy pools like Tornado.Cash by identifying common relayer gas dispatchers (e.g. 0xRelay99B) "
        "and correlating leaf index deposit timings against withdrawal blocks, reducing the anonymity set from 10,000 to single-digit candidate targets."
    )
    t_dna = Table([[Paragraph(dna_desc, body_style)]], colWidths=[500])
    t_dna.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#fef2f2")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#fca5a5")),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_dna)
    story.append(Spacer(1, 10))
    
    # Section 3: Legal & Judicial Readiness
    story.append(Paragraph("3. Courtroom Admissibility &amp; Law Enforcement Integration", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    story.append(Paragraph(
        "<b>Section 91 / 102 CrPC Legal Framework:</b><br/>"
        "Under Indian Criminal Law, freezing cryptocurrency on centralized exchanges requires formal legal notices issued by Police Officers or Magistrates. "
        "CyberTrace automates this workflow by pre-populating deposit transaction hashes, internal memo UIDs, and estimated loss figures directly into Section 91 CrPC notice templates. "
        "All exported dossiers include SHA-256 cryptographic timestamps ensuring chain-of-custody compliance under the Indian Evidence Act.",
        body_style
    ))
    story.append(Spacer(1, 10))
    
    # Section 4: Live Links
    story.append(Paragraph("4. Access &amp; Repository Resources", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceBefore=2, spaceAfter=6))
    
    links_data = [
        [Paragraph("<b>GitHub Repository:</b>", body_style), Paragraph("<font color='#0066ff'><u>https://github.com/Hidayatulla268/CyberTrace</u></font>", body_style)],
        [Paragraph("<b>Live Website (GitHub Pages):</b>", body_style), Paragraph("<font color='#0066ff'><u>https://hidayatulla268.github.io/CyberTrace/</u></font>", body_style)],
        [Paragraph("<b>Documentation PDF:</b>", body_style), Paragraph("<font color='#0066ff'><u>CyberTrace_Platform_Guide.pdf</u></font>", body_style)]
    ]
    t_links = Table(links_data, colWidths=[160, 340])
    t_links.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_links)
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Enterprise PDF successfully generated: {output_path}")

if __name__ == '__main__':
    out_file = os.path.join(r"c:\Users\HP\OneDrive\Desktop\crypto", "CyberTrace_Platform_Guide.pdf")
    create_cybertrace_pdf(out_file)
