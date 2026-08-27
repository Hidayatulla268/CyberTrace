"""
CyberTrace - Abbreviations, Shortcuts & Forensics Terminology Guide PDF Generator
Compiles all platform acronyms, legal provisions, blockchain forensics abbreviations, 
UPI core banking shortcuts, and security terms into an executive reference guide.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas for dynamic total page count in headers and footers."""
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
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#475569"))

        # Header (pages 2+)
        if self._pageNumber > 1:
            self.drawString(36, 11 * 72 - 28, "CYBERTRACE • GLOSSARY OF ABBREVIATIONS & FORENSICS SHORTCUTS")
            self.drawRightString(8.5 * 72 - 36, 11 * 72 - 28, "SIH 2026 PS-26183 | I4C, MHA")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(36, 11 * 72 - 32, 8.5 * 72 - 36, 11 * 72 - 32)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 32, 8.5 * 72 - 36, 32)
        self.setFont("Helvetica", 8)
        self.drawString(36, 22, "Ministry of Home Affairs • Indian Cyber Crime Coordination Centre (I4C) • LEA Reference Manual")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * 72 - 36, 22, page_text)
        self.restoreState()


def create_shortcuts_pdf():
    output_pdf = "CyberTrace_Abbreviations_and_Shortcuts_Guide.pdf"

    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=38,
        bottomMargin=38
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a'),
        alignment=1
    )

    sub_title = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155'),
        alignment=1
    )

    pill_style = ParagraphStyle(
        'TopPill',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0284c7'),
        alignment=1
    )

    sec_header = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#0f172a')
    )

    sec_desc = ParagraphStyle(
        'SectionDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#475569')
    )

    tbl_hdr = ParagraphStyle(
        'TableHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#ffffff')
    )

    abbr_style = ParagraphStyle(
        'AbbrStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0284c7')
    )

    fullform_style = ParagraphStyle(
        'FullFormStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0f172a')
    )

    meaning_style = ParagraphStyle(
        'MeaningStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.5,
        textColor=colors.HexColor('#334155')
    )

    elements = []

    # =========================================================================
    # HEADER BANNER
    # =========================================================================
    elements.append(Paragraph("SMART INDIA HACKATHON 2026 &bull; PROBLEM STATEMENT PS-26183", pill_style))
    elements.append(Paragraph("Ministry of Home Affairs &bull; Indian Cyber Crime Coordination Centre (I4C)", pill_style))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph("🛡️ CyberTrace — Master Glossary of Terms &amp; Shortcuts", title_style))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("Comprehensive Guide to All Abbreviations, Legal Statutes, Crypto Forensics Acronyms &amp; Banking Rails Shortcuts", sub_title))
    elements.append(Spacer(1, 10))

    # Overview Box
    intro_p = Paragraph(
        "<b>Executive Overview:</b> This reference compendium provides official definitions, statutory expansions, and contextual meanings for all technical short forms and abbreviations used throughout the <b>CyberTrace Enterprise Forensics Platform</b>. It is formatted as an operational quick-reference manual for Law Enforcement Officers (LEAs), I4C investigators, cyber analysts, and technical evaluators.",
        meaning_style
    )
    intro_table = Table([[intro_p]], colWidths=[540])
    intro_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f0f9ff')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#0284c7')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    elements.append(intro_table)
    elements.append(Spacer(1, 12))

    # Helper function to build clean tables
    def build_table(header_title, header_desc, col_widths, header_color, row_data):
        res = []
        res.append(Paragraph(header_title, sec_header))
        res.append(Paragraph(header_desc, sec_desc))
        res.append(Spacer(1, 5))

        formatted_rows = [
            [
                Paragraph("<b>Shortcut / Term</b>", tbl_hdr),
                Paragraph("<b>Full Form / Statutory Expansion</b>", tbl_hdr),
                Paragraph("<b>Meaning &amp; Operational Context in CyberTrace</b>", tbl_hdr)
            ]
        ]

        for item in row_data:
            formatted_rows.append([
                Paragraph(item[0], abbr_style),
                Paragraph(item[1], fullform_style),
                Paragraph(item[2], meaning_style)
            ])

        tbl = Table(formatted_rows, colWidths=col_widths, repeatRows=1)
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(header_color)),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor(header_color)),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#ffffff'), colors.HexColor('#f8fafc')]),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        res.append(tbl)
        res.append(Spacer(1, 14))
        return res

    # =========================================================================
    # TABLE 1: LAW ENFORCEMENT, LEGAL & STATUTORY ABBREVIATIONS
    # =========================================================================
    t1_data = [
        ("SIH", "Smart India Hackathon", "The nationwide innovation initiative by Ministry of Education / AICTE under which this solution is developed."),
        ("PS / PS-26183", "Problem Statement #26183", "The official MHA / I4C problem statement: 'Real-Time Identification of Fraud-Linked Crypto Exchanges & Banking Rails'."),
        ("I4C", "Indian Cyber Crime Coordination Centre", "The apex coordinating agency under Ministry of Home Affairs (MHA) for national cybercrime operations."),
        ("MHA", "Ministry of Home Affairs", "The nodal Government of India ministry governing internal security, central police forces, and cyber coordination."),
        ("CIS", "Cyber & Information Security Division", "The dedicated cyber division inside MHA overseeing national cyber incident response and I4C infrastructure."),
        ("LEA", "Law Enforcement Agency", "Police cyber cells, CID, CBI, ED, and special investigation teams utilizing CyberTrace for digital evidence tracing."),
        ("FIR", "First Information Report", "The formal legal document prepared by Indian police upon receiving information of a cognizable cyber offence."),
        ("NCRP", "National Cyber Crime Reporting Portal", "The central portal (cybercrime.gov.in) where citizens file complaints regarding online financial fraud and cyber threats."),
        ("1930 Helpline", "Citizen Financial Cyber Fraud Helpline", "National toll-free emergency helpline for reporting instant banking and UPI fraud for quick freeze intervention."),
        ("CrPC", "Code of Criminal Procedure, 1973", "The primary Indian procedural statute governing criminal investigation, asset seizure, and evidence collection."),
        ("Section 91 CrPC", "Summons to Produce Document or Thing", "Statutory police order commanding banks, telecom operators, or crypto exchanges to preserve logs and freeze funds."),
        ("BNSS / Sec 94", "Bharatiya Nagarik Suraksha Sanhita, 2023", "India's updated criminal procedural law replacing CrPC; Section 94 corresponds to summons and asset freeze orders."),
        ("IEA Sec 65B", "Section 65B, Indian Evidence Act, 1872", "Mandatory legal certificate required for electronic digital evidence (server logs, hashes) to be admissible in court."),
        ("BSA", "Bharatiya Sakshya Adhiniyam, 2023", "India's modernized law of evidence replacing the Indian Evidence Act, with upgraded digital evidence rules."),
        ("Sec 69A IT Act", "Section 69A, Information Technology Act, 2000", "Statutory power empowering CERT-In / DoT to issue emergency domain blocking and DNS sinkholing orders against cyber fraud URLs."),
        ("CERT-In", "Indian Computer Emergency Response Team", "National nodal agency under MeitY for cyber threat response, vulnerability mitigation, and emergency takedown coordination."),
        ("DoT", "Department of Telecommunications", "Ministry of Communications department directing ISPs (Jio/Airtel/Vi/BSNL) to execute nationwide IP/DNS blocking orders."),
        ("FIU-IND", "Financial Intelligence Unit – India", "National agency receiving and analyzing Suspicious Transaction Reports (STRs) and Cash Transaction Reports (CTRs)."),
        ("OFAC", "Office of Foreign Assets Control (US Treasury)", "Administers and enforces global economic sanctions, blacklisting illicit crypto mixer addresses and state hackers."),
        ("SDN List", "Specially Designated Nationals and Blocked Persons", "Global sanctions database of sanctioned terror financiers, state-sponsored cybercartels, and illicit crypto wallets."),
        ("MLAT", "Mutual Legal Assistance Treaty", "Bilateral treaties between governments allowing cross-border evidence gathering and international exchange freeze requests."),
        ("CLOUD Act", "Clarifying Lawful Overseas Use of Data Act (US)", "Allows foreign law enforcement to request expedited data preservation from US-headquartered crypto VASPs."),
        ("KYC", "Know Your Customer", "Mandatory customer identification verification (Aadhaar, PAN, Passport) required for all bank and registered VASP accounts."),
        ("AML / CFT", "Anti-Money Laundering / Countering Financing of Terrorism", "Statutory regulatory compliance framework designed to detect, freeze, and prevent illicit movement of capital."),
        ("VASP", "Virtual Asset Service Provider", "Any entity conducting cryptocurrency exchange, transfer, custody, or conversion services (Binance, CoinDCX, etc.)."),
        ("IFSO", "Intelligence Fusion & Strategic Operations", "The specialized cyber investigation unit of the Delhi Police Special Cell investigating organized syndicates."),
        ("CID", "Criminal Investigation Department", "Specialized crime investigation wing of state police forces.")
    ]

    elements.extend(build_table(
        "⚖️ 1. Law Enforcement, Legal Statutes & Governance Terms",
        "Statutory provisions, law enforcement agencies, and legal frameworks governing evidence collection and account freezing.",
        [75, 145, 320],
        "#0369a1",
        t1_data
    ))

    elements.append(PageBreak())

    # =========================================================================
    # TABLE 2: BLOCKCHAIN & CRYPTOCURRENCY FORENSICS TERMS
    # =========================================================================
    t2_data = [
        ("RPC / JSON-RPC", "Remote Procedure Call Protocol", "Communication protocol used by app.js to communicate directly with live blockchain nodes (ETH, BSC, Polygon, Solana)."),
        ("EVM", "Ethereum Virtual Machine", "The decentralized smart contract runtime engine shared across Ethereum, Polygon, BNB Chain, and Arbitrum."),
        ("ETH / BTC / USDT", "Ethereum / Bitcoin / Tether USD", "Core cryptocurrency tokens analyzed in forensic fund flows (Ether, Bitcoin, and USD-pegged stablecoins)."),
        ("TRX / SOL / BNB", "TRON / Solana / Binance Coin", "Native high-throughput blockchain tokens commonly used in fast scam dispersion and cross-chain hops."),
        ("POL / MATIC", "Polygon Ecosystem Token", "Layer-2 scaling token used for low-cost token laundering and permit2 batch draining."),
        ("Burner Wallet", "Single-Use Disposable Scam Wallet", "Temporary address generated for a single victim heist, swept to ₹0.00 within seconds and abandoned on-chain."),
        ("Gas Ancestry", "Backward Genesis Gas Lineage Tracing", "Forensic technique tracing backward to the initial gas fee transaction that funded the burner wallet, identifying parent KYC exchange accounts."),
        ("Sweep Tx", "Automated Outflow Liquidation Transfer", "Rapid automated transaction draining 100% of victim funds into intermediary mules or terminal exchange deposit clusters."),
        ("Peeling Chain", "Peeling Chain Laundering Topology", "Multi-hop layering technique splitting funds into small tranches across intermediate hops (e.g. 60/40 ratio) to avoid fixed threshold alerts."),
        ("CEX", "Centralized Exchange", "Custodial platforms (Binance, WazirX, OKX, KuCoin) where criminals attempt to convert illicit crypto into fiat currency."),
        ("DEX", "Decentralized Exchange", "Peer-to-peer automated liquidity smart contracts (Uniswap, PancakeSwap) without KYC or central management."),
        ("DeFi", "Decentralized Finance", "Blockchain-based financial ecosystem offering lending, staking, and liquidity pools without intermediaries."),
        ("DApp", "Decentralized Application", "Web3 application running on decentralized smart contract infrastructure, often spoofed by phishing syndicates."),
        ("UTXO", "Unspent Transaction Output", "Bitcoin's accounting model where unspent outputs are combined and split across multi-input transactions."),
        ("TX / TXID", "Transaction / Transaction Identifier", "The unique 64-character hexadecimal cryptographic hash proving an immutable transfer of funds on-chain."),
        ("OTC", "Over-The-Counter Trading Desk", "Private peer-to-peer brokered trades executed outside public order books to liquidate large scam tranches into cash."),
        ("P2P", "Peer-to-Peer", "Direct user-to-user transfers on crypto exchange marketplaces, frequently abused by mule networks."),
        ("ERC-20 / TRC-20", "Token Standards (Ethereum / TRON)", "Technical specifications for smart contract tokens (e.g. USDT on Ethereum vs USDT on TRON network)."),
        ("BEP-20", "BNB Smart Chain Token Standard", "Technical smart contract token standard running on the Binance Smart Chain ecosystem."),
        ("Permit2", "Permit2 Signature Protocol", "Token approval standard exploited by 'Phantom-Drainer' phishing attacks for gasless multi-token wallet drainage."),
        ("Multi-Sig", "Multi-Signature Crypto Vault", "Smart contract wallet requiring M-of-N private key cryptographic signatures to approve any outbound fund transfer."),
        ("APT / APT-38", "Advanced Persistent Threat (Lazarus Group)", "State-sponsored cyber espionage and financial theft syndicate operating on behalf of DPRK (North Korea)."),
        ("DPRK", "Democratic People's Republic of Korea", "North Korea; designated state sponsor of cyber operations targeting decentralized protocols and exchanges."),
        ("Relayer", "Gas Relayer Dispatcher", "Third-party proxy service that broadcasts transactions and pays gas fees for users, demasking Tornado.Cash users."),
        ("CoinJoin", "CoinJoin Transaction Obfuscator", "Bitcoin privacy technique combining payments from multiple parties into a single multi-input/output transaction."),
        ("Fraud DNA™", "Behavioral Sequence Fingerprinting", "CyberTrace proprietary 8-dimensional algorithm matching zero-day wallets to known crime syndicate campaign signatures.")
    ]

    elements.extend(build_table(
        "₿ 2. Blockchain, Cryptocurrency & Forensics Analytics Terms",
        "Technical blockchain protocols, token standards, obfuscation mechanisms, and forensic pattern recognition acronyms.",
        [85, 145, 310],
        "#7c3aed",
        t2_data
    ))

    elements.append(PageBreak())

    # =========================================================================
    # TABLE 3: UPI & INDIAN CORE BANKING FORENSICS TERMS (MODE 2)
    # =========================================================================
    t3_data = [
        ("UPI", "Unified Payments Interface", "Instant real-time payment system developed by NPCI facilitating inter-bank peer-to-peer and merchant transactions."),
        ("NPCI", "National Payments Corporation of India", "The umbrella organization managing retail payment and settlement systems (UPI, IMPS, RuPay, AePS) in India."),
        ("VPA", "Virtual Payment Address", "Unique financial identifier (e.g. daily.payout@oksbi, CBI.fund@okaxis) linked directly to underlying bank accounts."),
        ("UTR", "Unique Transaction Reference Number", "A 12-to-22-character unique alphanumeric reference generated for tracking every banking transaction across India."),
        ("IFSC", "Indian Financial System Code", "An 11-character alphanumeric code (e.g. SBIN0001245) identifying specific bank branches across the country."),
        ("IMPS", "Immediate Payment Service", "Instant 24/7 electronic funds transfer rail operated by NPCI for inter-bank domestic remittances."),
        ("NEFT", "National Electronic Funds Transfer", "Batch-settled nationwide electronic fund transfer system maintained by the Reserve Bank of India (RBI)."),
        ("RTGS", "Real Time Gross Settlement", "Continuous, gross real-time settlement system for high-value domestic financial transactions above ₹2 Lakh."),
        ("CBS", "Core Banking Solution / Core Banking System", "Centralized bank software backend (e.g. Finacle, BaNCS) maintaining master customer ledgers and branch transactions."),
        ("AA Framework", "Account Aggregator Framework", "RBI-regulated consent-based financial data-sharing network enabling real-time digitally certified bank statement retrieval."),
        ("CKYC", "Central Know Your Customer Registry", "Centralized Indian repository storing verified customer KYC records across banks, mutual funds, and insurers."),
        ("RBI", "Reserve Bank of India", "The central bank of India exercising regulatory supervision over banks, payment operators, and NBFCs."),
        ("POS", "Point of Sale Terminal", "Electronic card swipe / merchant device where scammers execute rapid fraudulent merchandise purchases for cash-out."),
        ("ATM", "Automated Teller Machine", "Cash dispensing terminal where Layer-2/Layer-3 mule account holders execute physical cash withdrawals."),
        ("APK", "Android Package Kit", "Android app installer file; weaponized by scammers in remote-access phishing and fake customer support scams."),
        ("QR Code", "Quick Response Matrix Barcode", "Two-dimensional barcode scanned by mobile banking apps for instantaneous merchant and P2P payments.")
    ]

    elements.extend(build_table(
        "📱 3. UPI & Core Banking Rails Forensics Terms (Mode 2)",
        "Indian payment rails, banking infrastructure, clearing systems, and mule account tracking terminology.",
        [80, 145, 315],
        "#059669",
        t3_data
    ))

    # =========================================================================
    # TABLE 4: SOFTWARE ARCHITECTURE, WEB & SECURITY TERMS
    # =========================================================================
    t4_data = [
        ("SPA", "Single Page Application", "Web architecture where UI updates dynamically without full page reloads, providing fast forensic graph response."),
        ("SVG", "Scalable Vector Graphics", "XML-based vector image standard utilized in CyberTrace for rendering interactive fund flow graphs and world flight maps."),
        ("XSS", "Cross-Site Scripting", "Web vulnerability where malicious scripts are executed; prevented via OWASP sanitization in security.js."),
        ("CSRF", "Cross-Site Request Forgery", "Attack forcing unauthorized actions on a trusted web application; guarded against via origin checks and dynamic nonces in security.js."),
        ("CSP", "Content Security Policy", "HTTP security header restricting sources of scripts, styles, fonts, and network connections in index.html."),
        ("OWASP", "Open Web Application Security Project", "International standard body defining web application security benchmarks and defensive coding practices."),
        ("BIP-39", "Bitcoin Improvement Proposal 39", "Standard mnemonic phrase format using 12/24 word dictionaries to generate master crypto wallet private keys."),
        ("Anti-Seed Shield", "Anti-Seed-Phrase Harvester Subsystem", "Real-time clipboard and input listener in security.js intercepting accidental mnemonic exposure and protecting citizen wallets."),
        ("Frame-Busting", "Anti-Clickjacking Runtime Defense", "JavaScript enforcement ensuring CyberTrace cannot be embedded inside malicious third-party iframes (top === self)."),
        ("Self-XSS", "Console Social Engineering Attack", "Deceptive attack where scammers ask victims to paste malicious scripts in F12 console; intercepted and blocked by security.js."),
        ("SHA-256", "Secure Hash Algorithm 256-Bit", "Cryptographic one-way hash algorithm generating 64-character digital fingerprints for evidence dossiers."),
        ("DOM", "Document Object Model", "Tree structure of HTML elements manipulated by app.js during live blockchain and banking rail analysis."),
        ("API", "Application Programming Interface", "Set of protocols and endpoints enabling software systems to exchange data (e.g. CoinGecko, TronGrid)."),
        ("HUD", "Heads-Up Display", "Visual dashboard layout displaying real-time telemetry, risk gauges, and price tickers in high-contrast panels."),
        ("USP", "Unique Selling Proposition", "The defining advantages of CyberTrace: Dual Mode (Crypto+UPI), automated Section 91 notices, and zero cost for LEAs.")
    ]

    elements.extend(build_table(
        "🛡️ 4. Software Architecture & Enterprise Web Security Terms",
        "Web engineering, cryptographic algorithms, cybersecurity defenses, and application interface definitions.",
        [80, 145, 315],
        "#d97706",
        t4_data
    ))

    # =========================================================================
    # TABLE 5: BUILT-IN CRIME SYNDICATE CAMPAIGN IDENTIFIERS
    # =========================================================================
    t5_data = [
        ("CYB-2048", "'Hydra-Peel' Syndicate", "Telegram task-based part-time job scam featuring 3-hop automated 80/20 peeling chains into WazirX / Binance off-ramps."),
        ("CYB-3912", "'Phantom-Drainer' Syndicate", "Permit2 phishing DApp drainer network using sub-15s multi-token drains and Cross-Chain Bridges into Tornado Cash."),
        ("CYB-1084", "'Golden-Boar' Syndicate", "Pig butchering fake high-yield liquidity arbitrage scam using staged deposit warming and OKX/KuCoin memo routing."),
        ("Lazarus APT-38", "State-Sponsored Hack Preset", "State-backed multi-sig contract drain involving Tornado.Cash 100 ETH mixer pools and Dubai OTC broker cash-out."),
        ("Digital Arrest", "Police Impersonation Syndicate", "Coercive extortion scheme impersonating CBI/Customs officials, routing victim funds into Axis/SBI mule accounts.")
    ]

    elements.extend(build_table(
        "🕵️ 5. Built-In Crime Syndicate Campaign Identifiers (Fraud DNA™)",
        "Standardized crime campaign codes and modus operandi signatures recognized by the Fraud DNA™ engine.",
        [90, 140, 310],
        "#dc2626",
        t5_data
    ))

    # Build Document
    print(f"Compiling Shortcuts PDF: {output_pdf} ...")
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {output_pdf} ({os.path.getsize(output_pdf)} bytes)")


if __name__ == "__main__":
    create_shortcuts_pdf()
