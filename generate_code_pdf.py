"""
CyberTrace - Complete Source Code PDF Generator
Compiles all codebase source files into a single publication-grade PDF document:
- README.md (Architecture & Documentation)
- index.html (Single Page Application & DOM Structure)
- app.js (Forensics Engine, Live RPCs, Map, Graphs, Tranche Tracking)
- security.js (Enterprise 15-Layer Security Shield)
- style.css (Forensic HUD & Responsive Styling)
"""

import os
import sys
import hashlib
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted, KeepTogether, HRFlowable
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
        if self._pageNumber == 1:
            return  # Suppress header/footer on cover page

        self.saveState()
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(colors.HexColor("#475569"))

        # Top Header
        self.drawString(36, 11 * 72 - 28, "CYBERTRACE • COMPLETE ENTERPRISE SOURCE CODE REPOSITORY")
        self.drawRightString(8.5 * 72 - 36, 11 * 72 - 28, "SIH 2026 • PS-26183 | I4C, MHA")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 11 * 72 - 32, 8.5 * 72 - 36, 11 * 72 - 32)

        # Bottom Footer
        self.line(36, 32, 8.5 * 72 - 36, 32)
        self.setFont("Helvetica", 7.5)
        self.drawString(36, 22, "Ministry of Home Affairs • Indian Cyber Crime Coordination Centre (I4C) • Confidential LEA Repository")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * 72 - 36, 22, page_text)
        self.restoreState()


def wrap_code_lines(content, max_len=115):
    """Wraps long source code lines cleanly with continuation markers."""
    out_lines = []
    raw_lines = content.splitlines()
    line_num = 1
    for raw in raw_lines:
        line_str = raw.replace('\t', '    ')
        if len(line_str) <= max_len:
            out_lines.append(f"{line_num:5d} | {line_str}")
        else:
            # Wrap long line
            first_chunk = line_str[:max_len]
            out_lines.append(f"{line_num:5d} | {first_chunk}")
            remaining = line_str[max_len:]
            while remaining:
                chunk = remaining[:max_len - 8]
                out_lines.append(f"      |   ↳ {chunk}")
                remaining = remaining[max_len - 8:]
        line_num += 1
    return out_lines


def generate_source_code_pdf():
    output_pdf = "CyberTrace_Complete_Source_Code.pdf"
    workspace_dir = os.path.dirname(os.path.abspath(__file__))

    # Target source files
    source_files = [
        {
            "filename": "README.md",
            "path": os.path.join(workspace_dir, "README.md"),
            "category": "Project Documentation & Architecture Specification",
            "desc": "System architecture, dual-engine topology, crime testing presets, global platform comparison matrix, and production scaling roadmap."
        },
        {
            "filename": "index.html",
            "path": os.path.join(workspace_dir, "index.html"),
            "category": "Frontend UI & DOM Layout",
            "desc": "Complete Single Page Application (SPA) structure, security headers, HUD cards, SVG canvas zones, live tickers, and modal dialogues."
        },
        {
            "filename": "app.js",
            "path": os.path.join(workspace_dir, "app.js"),
            "category": "Core Forensics Logic & RPC Gateway",
            "desc": "Live multi-chain blockchain RPC ingestion, CoinGecko price oracle, dynamic SVG fund graphs, cartographic map flight paths, time-travel scrubber, and Section 91 CrPC generator."
        },
        {
            "filename": "security.js",
            "path": os.path.join(workspace_dir, "security.js"),
            "category": "Enterprise Security Defense Layer",
            "desc": "15-layer client-side security shield: Prototype pollution freezing, OWASP XSS sanitizer, token-bucket rate limiting, and SHA-256 evidence hashing."
        },
        {
            "filename": "style.css",
            "path": os.path.join(workspace_dir, "style.css"),
            "category": "Styling & Responsive Forensic Design System",
            "desc": "Custom dark-mode cyber forensics design system, glassmorphism tokens, glowing radar animations, and responsive HUD grids."
        }
    ]

    # Collect statistics
    total_lines = 0
    total_bytes = 0
    file_stats = []

    for item in source_files:
        if os.path.exists(item["path"]):
            size = os.path.getsize(item["path"])
            with open(item["path"], "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
                lines = len(content.splitlines())
                sha256 = hashlib.sha256(content.encode("utf-8")).hexdigest()
            total_lines += lines
            total_bytes += size
            file_stats.append({
                "name": item["filename"],
                "category": item["category"],
                "desc": item["desc"],
                "lines": lines,
                "bytes": size,
                "sha256": sha256,
                "content": content
            })
        else:
            print(f"Warning: {item['path']} not found.")

    # Setup Document
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
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#0f172a'),
        alignment=1
    )
    
    sub_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#334155'),
        alignment=1
    )

    badge_style = ParagraphStyle(
        'CoverBadge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#0284c7'),
        alignment=1
    )

    sec_title = ParagraphStyle(
        'FileHeaderTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0f172a')
    )

    sec_sub = ParagraphStyle(
        'FileHeaderSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#475569')
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        fontName='Courier',
        fontSize=6.0,
        leading=7.2,
        textColor=colors.HexColor('#1e293b')
    )

    elements = []

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("SMART INDIA HACKATHON 2026 &bull; PROBLEM STATEMENT PS-26183", badge_style))
    elements.append(Paragraph("Ministry of Home Affairs &bull; Indian Cyber Crime Coordination Centre (I4C)", badge_style))
    elements.append(Spacer(1, 14))
    elements.append(Paragraph("🛡️ CyberTrace", title_style))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph("Complete Production Source Code Repository &amp; Technical Implementation", sub_style))
    elements.append(Spacer(1, 14))

    # Summary Meta Box
    summary_data = [
        [
            Paragraph("<b>Repository:</b> Hidayatulla268/CyberTrace", sec_sub),
            Paragraph("<b>Status:</b> Production Ready v8.5", sec_sub)
        ],
        [
            Paragraph(f"<b>Total Source Files:</b> {len(file_stats)} Core Files", sec_sub),
            Paragraph(f"<b>Total Lines of Code:</b> {total_lines:,} LOC", sec_sub)
        ],
        [
            Paragraph(f"<b>Codebase Footprint:</b> {total_bytes / 1024:.1f} KB", sec_sub),
            Paragraph(f"<b>Generated On:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", sec_sub)
        ],
        [
            Paragraph("<b>License:</b> MIT Open Source", sec_sub),
            Paragraph("<b>Target Audience:</b> I4C / LEA Technical Reviewers", sec_sub)
        ]
    ]

    summary_table = Table(summary_data, colWidths=[260, 260])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 16))

    # TABLE OF CONTENTS
    elements.append(Paragraph("<b>SOURCE CODE REPOSITORY INDEX &amp; METRICS</b>", sec_title))
    elements.append(Spacer(1, 6))

    toc_data = [
        [
            Paragraph("<b>#</b>", sec_sub),
            Paragraph("<b>File Name</b>", sec_sub),
            Paragraph("<b>Category / Description</b>", sec_sub),
            Paragraph("<b>Lines</b>", sec_sub),
            Paragraph("<b>Size</b>", sec_sub)
        ]
    ]

    for idx, stat in enumerate(file_stats, start=1):
        toc_data.append([
            Paragraph(f"<b>{idx}</b>", sec_sub),
            Paragraph(f"<code>{stat['name']}</code>", sec_sub),
            Paragraph(f"<b>{stat['category']}</b><br/>{stat['desc']}", sec_sub),
            Paragraph(f"{stat['lines']:,}", sec_sub),
            Paragraph(f"{stat['bytes'] / 1024:.1f} KB", sec_sub)
        ])

    toc_table = Table(toc_data, colWidths=[24, 90, 290, 50, 66])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e0f2fe')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#0284c7')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    elements.append(toc_table)

    elements.append(Spacer(1, 16))
    elements.append(Paragraph("<b>CRYPTOGRAPHIC INTEGRITY &amp; TAMPER-PROOF EVIDENCE (SECTION 65B IEA / BSA 2023)</b>", sec_title))
    elements.append(Spacer(1, 4))

    hash_data = [
        [Paragraph("<b>File</b>", sec_sub), Paragraph("<b>SHA-256 Digest</b>", sec_sub)]
    ]
    for stat in file_stats:
        hash_data.append([
            Paragraph(f"<code>{stat['name']}</code>", sec_sub),
            Paragraph(f"<font name='Courier' size='6.5'>{stat['sha256']}</font>", sec_sub)
        ])

    hash_table = Table(hash_data, colWidths=[90, 430])
    hash_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f1f5f9')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#94a3b8')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(hash_table)

    elements.append(PageBreak())

    # =========================================================================
    # SOURCE CODE LISTINGS (CHUNKED PREFORMATTED FOR MAXIMUM SPEED)
    # =========================================================================
    for stat in file_stats:
        # File Section Banner
        banner_data = [
            [
                Paragraph(f"📄 <b>FILE: {stat['name']}</b>", ParagraphStyle('BTitle', fontName='Helvetica-Bold', fontSize=12, textColor=colors.HexColor('#0f172a'))),
                Paragraph(f"<b>Lines:</b> {stat['lines']:,} &nbsp;|&nbsp; <b>Size:</b> {stat['bytes']/1024:.1f} KB", ParagraphStyle('BStats', fontName='Helvetica-Bold', fontSize=9, textColor=colors.HexColor('#0369a1'), alignment=2))
            ],
            [
                Paragraph(f"<b>Category:</b> {stat['category']}<br/><b>Purpose:</b> {stat['desc']}", sec_sub),
                Paragraph(f"<b>SHA-256:</b> <font name='Courier' size='6'>{stat['sha256'][:28]}...</font>", sec_sub)
            ]
        ]
        banner_table = Table(banner_data, colWidths=[340, 180])
        banner_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f0f9ff')),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#0284c7')),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#bae6fd')),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        
        elements.append(banner_table)
        elements.append(Spacer(1, 6))

        # Format lines with line numbers
        wrapped_lines = wrap_code_lines(stat['content'], max_len=118)

        # Chunk into blocks of 70 lines per Preformatted to ensure fast ReportLab flowable layout
        CHUNK_SIZE = 70
        for i in range(0, len(wrapped_lines), CHUNK_SIZE):
            chunk = "\n".join(wrapped_lines[i:i + CHUNK_SIZE])
            elements.append(Preformatted(chunk, code_style))

        elements.append(PageBreak())

    print(f"Building PDF: {output_pdf} ...")
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {output_pdf} ({os.path.getsize(output_pdf)} bytes)")


if __name__ == "__main__":
    generate_source_code_pdf()
