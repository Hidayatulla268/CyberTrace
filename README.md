# 🛡️ CyberTrace — Real-Time Crypto Forensics & Anti-Fraud Intelligence Platform

> **Smart India Hackathon 2026 &bull; Problem Statement PS-26183**  
> *Ministry of Home Affairs &bull; Indian Cyber Crime Coordination Centre (I4C)*  
> **Title:** Real-Time Identification of Fraud-Linked Cryptocurrency Exchanges from Victim-Reported Suspect Wallet Addresses through Automated Blockchain Analytics

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![SIH-2026](https://img.shields.io/badge/SIH-2026%20PS--26183-orange.svg)](https://www.sih.gov.in)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Web%20%7C%20Vanilla%20JS%20%7C%20CSS3-cyan.svg)]()

---

## 🌟 Core USP (Unique Selling Proposition)

$$\mathbf{Report} \longrightarrow \mathbf{Trace} \longrightarrow \mathbf{Connect} \longrightarrow \mathbf{Identify} \longrightarrow \mathbf{Monitor} \longrightarrow \mathbf{Prove}$$

> **“From a single victim-reported wallet address, automatically trace the stolen funds, identify their destination exchanges, uncover connected accomplice wallets, monitor further movement in real-time, and generate court-ready Section 91 CrPC forensic evidence.”**

---

## 🚀 Key Features & Capabilities

### 1. 🔍 Smart Wallet Scanner
- Instant address scanning across major blockchains (Ethereum, BSC, Tron, Polygon).
- Aggregates multi-token balances (USDT, ETH, BTC, TRX, INR Equivalent).
- Displays complete blockchain transaction ledgers with 1-click copyable hashes and timestamps.

### 2. 💰 Stolen Money Tracker (Tranche Following Engine)
- Follows specific victim deposit transactions (e.g. ₹50,000 or ₹1,00,000) hop-by-hop.
- Calculates exact peeling ratios and retention percentages across splitting paths (e.g. 100% &rarr; 60%/40% &rarr; 36%/24% &rarr; CEX Sweep).
- 1-click export of complete money trail CSV logs for evidentiary submissions.

### 3. 🕸️ Interactive Fund-Flow Graph
- Dynamic SVG graph visualizing the complete money laundering lifecycle:  
  $$\text{Victim Account} \longrightarrow \text{Suspect Hub} \longrightarrow \text{Layer 1 Splitter} \longrightarrow \text{Exchange Cluster (CEX)}$$
- Animated particle flows, interactive node inspection, and full-screen pan & zoom exploration.

### 4. 🏦 Centralized Exchange Finder & Nodal Directory
- Heuristic AI identification of Centralized Exchanges (Binance Hot Cluster 14, WazirX India Gateway, KuCoin, OKX) with confidence metrics (e.g. 91% Confidence).
- Built-in directory of Exchange Law Enforcement Nodal contacts for rapid FIR subpoena dispatch.

### 5. 🔗 Hidden & Connected Wallet Detector
- Automatically reveals unlisted accomplice infrastructure connected to the suspect:
  - **Peeling Chain Splitters:** Intermediary layer-1 and layer-2 child nodes.
  - **Gas Sponsor Relayers:** Shared funding originators and relayer dispatchers.
  - **Co-Spending Mules:** Addresses co-spending UTXOs or batching token permits.
  - **Fraud DNA Twins:** Correlated campaign accomplice nodes.

### 6. 🚨 Heuristic AI Risk Score Gauge (0–100)
- Instant threat level calculation (Low, Medium, High, Critical Risk) using a dynamic semi-circular gauge.
- Forensic breakdown with clear, actionable suspicion indicators.

### 7. 🧠 Automated Fraud Pattern Recognition
- Real-time classification of complex money laundering techniques:
  - **Peeling Chains:** High-velocity sequential token peeling.
  - **Sub-Minute Sweeps:** Automated scripts moving funds in $<45$ seconds.
  - **Fan-Out / Fan-In:** Layering dispersion followed by centralized consolidation.
  - **Mixer Contracts:** Tornado.Cash and cross-chain bridge hopping.

### 8. 🧬 Fraud DNA™ — Behavioral Campaign Syndicate Attribution
- Identifies **zero-day unknown scam wallets** with zero prior police reports by comparing their behavioral sequence fingerprints against known crime syndicates:
  - **Campaign #CYB-2048 ("Hydra-Peel"):** Telegram Task & Part-Time Job Scams.
  - **Campaign #CYB-3912 ("Phantom-Drainer"):** Permit2 Phishing DApp Drainers.
  - **Campaign #CYB-1084 ("Golden-Boar"):** Fake High-Yield Pig Butchering Scams.
- Displays an interactive **Lineage Tree Visualizer** and **8-Dimensional Vector Radar Matrix** (Timing, Splitting, Topology, Amount, Destination, Gas).

### 9. ⏱️ Live Mempool Monitoring & Real-Time Alert Feed
- Continuous watching of flagged addresses with live visual pulse beacons.
- Real-time ingestion stream simulation with auto-escalation to investigator watchlists.

### 10. 📋 Victim Fraud Reporting Portal
- Public and law enforcement intake portal to submit wallet address, TXID, amount lost, and fraud category.
- Instantly auto-generates a national reference number (e.g. `I4C-2026-XXXXXX`) and initiates automated tracing.

### 11. 🧾 Auto Evidence Report (Section 91 CrPC Compliant)
- 1-click generator for printable, court-ready **I4C Crypto Forensic Dossiers**.
- Includes complete suspect metadata, transaction ledgers, exchange attributions, Fraud DNA findings, and cryptographic SHA-256 integrity stamps.

### 12. 🌐 Public Wallet Safety Check ("Check Before You Send")
- Consumer-facing pre-transaction safety scanner for everyday crypto users.
- Gives instant **SAFE**, **CAUTION**, or **⛔ DO NOT SEND (SCAM)** verdicts with threat factor breakdowns to prevent scams before funds leave the victim's wallet.

### 13. 🕵️ Fraud Network Map (Cross-Case Syndicate Nexus)
- Correlates multiple independent victim complaints into an interconnected crime syndicate graph.
- Discovers shared laundering hubs, common OTC brokers, and unified exchange cash-out gateways linking separate cases.

---

## 🏛️ System Architecture

```
                                  [ Victim / 1930 Portal Ingestion ]
                                                 │
                                                 ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   CYBERTRACE FORENSICS CORE                                     │
├────────────────────────────────┬───────────────────────────────┬────────────────────────────────┤
│    BLOCKCHAIN INGESTION        │      BEHAVIORAL ENGINE        │       LEGAL & DISPATCH         │
│  • EVM / Tron / BTC Crawlers   │  • 8-D Vector Fraud DNA™      │  • Section 91 CrPC Subpoenas   │
│  • Mempool Watcher             │  • Peeling Chain Analyzer     │  • FIU-IND / I4C Dossier PDF   │
│  • Multi-Token Balances        │  • CEX Cluster Attribution    │  • Exchange Nodal Desks        │
└────────────────────────────────┴───────────────────────────────┴────────────────────────────────┘
                                                 │
                                                 ▼
[ 🔍 Smart Scanner ] ── [ 💰 Stolen Tracker ] ── [ 🧬 Fraud DNA™ ] ── [ 🕵️ Network Map ] ── [ 🧾 Dossier ]
```

---

## 🖥️ Live Judges Demo Walkthrough (1-Click Tour)

The top navigation header features a built-in step-by-step judge demonstration tour:

1. **Step 1: Address** &rarr; Enters suspect wallet address (`0xA1b2C3d4E5f6G7h8I9j0K1L2m3N4o5P6q7R8s9T0`).
2. **Step 2: Analyze** &rarr; Executes automated blockchain multi-hop trace.
3. **Step 3: Risk Score** &rarr; Inspects the 87/100 High Risk AI score and evidence checklist.
4. **Step 4: Flow Graph** &rarr; Highlights the multi-hop fund-flow graph.
5. **Step 5: Exchange Detection** &rarr; Pinpoints Binance Hot Cluster 14 (91% confidence).
6. **Step 6: Fraud DNA™** &rarr; Demonstrates zero-day detection on unreported Wallet Z (91% match with Campaign #CYB-2048).
7. **Step 7: Dossier** &rarr; Opens the court-ready printable Section 91 CrPC forensic report.

---

## 💻 Tech Stack

- **Frontend:** Semantic HTML5, Vanilla JavaScript (ES6+), Vanilla CSS3 (Custom Glassmorphic Dark Design System)
- **Visualization:** Native Responsive SVG Engines, Dynamic Bezier Particle Flow Lines, Matrix Radars
- **Zero External Runtime Dependencies:** Runs natively in any modern web browser without heavy build steps.

---

## 🛠️ Quick Start & Installation

### Option 1: Direct Browser Launch
Simply clone this repository and open `index.html` in any modern web browser:
```bash
git clone https://github.com/Hidayatulla268/CyberTrace.git
cd CyberTrace
# Double click index.html or open via terminal:
# Windows:
start index.html
# Mac:
open index.html
# Linux:
xdg-open index.html
```

### Option 2: Run via Local Dev Server
```bash
# Using Node / npx:
npx serve .

# Using Python 3:
python -m http.server 3000
```
Then navigate to `http://localhost:3000` in your browser.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <b>Developed for Smart India Hackathon 2026 (PS-26183)</b><br>
  <i>Indian Cyber Crime Coordination Centre (I4C) &bull; Ministry of Home Affairs</i>
</p>
