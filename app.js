/**
 * CyberTrace - Crypto Forensics Intelligence Platform
 * Solution Engine for Smart India Hackathon 2026 (Problem Statement 26183)
 * Full Master & Enterprise Feature Engine:
 * - 🔍 Smart Wallet Scanner
 * - 💰 Stolen Money Tracker (Tranche Tracer)
 * - 🕸️ Fund-Flow Graph (Multi-Hop Layering Visualizer)
 * - 🎯 Time-Travel Transaction Scrubber (MetaSleuth / Breadcrumbs)
 * - 🌉 Cross-Chain Bridge Tracker (TRM Labs / Chainalysis)
 * - 🏷️ Global Entity & Tag Directory (Arkham-grade 100k+ records)
 * - 🌪️ Mixer & Obfuscation Demasking Engine (Elliptic-grade)
 * - 🛡️ Global Sanctions & OFAC / FIU-IND Screener
 * - 💼 Case Management Workspace & Evidence Vault
 * - 📜 Automated Multi-Jurisdictional Subpoena Dispatcher (Section 91 CrPC)
 * - 🏦 Exchange Finder (Centralized Exchange Attribution)
 * - 🔗 Hidden Wallet Detector (Accomplice Infrastructure Discovery)
 * - 🚨 Fraud Risk Score (Heuristic AI 0-100 Gauge)
 * - 🧠 Fraud Pattern Detection (Peeling Chains & Fan-Out/Fan-In)
 * - 🧬 Fraud DNA™ (Behavioral Campaign Syndicate Attribution)
 * - ⏱️ Live Wallet Monitoring (Mempool Ingestion & Threat Watchlist)
 * - 📋 Fraud Reporting Portal (Victim Intake & FIR Generator)
 * - 🧾 Auto Evidence Report (Section 91 CrPC I4C Investigation Dossier)
 * - 🌐 Public Wallet Safety Check (Pre-Transaction Scam Screener)
 * - 🕵️ Fraud Network Map (Cross-Case Syndicate Nexus Graph)
 * - ⭐ Core USP Workflow (Report → Trace → Connect → Identify → Monitor → Prove)
 */

document.addEventListener('DOMContentLoaded', () => {
  // --- APPLICATION STATE ---
  const state = {
    currentView: 'dashboard',
    currentAddress: '0xA1b2C3d4E5f6G7h8I9j0K1L2m3N4o5P6q7R8s9T0',
    currentCampaignId: 'CYB-2048',
    currentTrancheId: 'tx-50k',
    caseId: 'CYB-2026-001245',
    zoomLevel: 1,
    panX: 0,
    panY: 0,
    isLiveMonitoring: true,
    liveInterval: null,
    scrubberPlaying: false,
    scrubberInterval: null,
    scrubberSpeed: 1,
    recentCases: [
      { id: 'I4C-2026-001245', target: '0xA1b2...9T0', loss: '₹50,000', type: 'Task-Based Telegram Scam', time: '10 mins ago', status: 'Active Tracing' },
      { id: 'I4C-2026-009812', target: '0x742d...f44e', loss: '₹34,50,000', type: 'Ransomware Extortion Outflow', time: '1 hour ago', status: 'Mixer Flagged' },
      { id: 'I4C-2026-003410', target: '0x8920...43e7', loss: '₹4,15,000', type: 'Pig Butchering Investment Scam', time: '3 hours ago', status: 'Subpoena Sent' },
      { id: 'I4C-2026-008819', target: '0xAB89...91F2', loss: '₹1,25,000', type: 'Fraud DNA Zero-Day Detection', time: 'Just now', status: 'DNA Matched (91%)' }
    ]
  };

  // --- KNOWN FRAUD DNA CAMPAIGNS REPOSITORY ---
  const campaignDNAProfiles = {
    'CYB-2048': {
      id: 'Campaign #CYB-2048',
      name: '"Hydra-Peel" Telegram Task Scam Syndicate',
      shortName: 'Hydra-Peel Syndicate',
      crimeCategory: 'Task-Based Part-Time Job Scam',
      matchPct: 91,
      totalLoss: '₹84,50,000+',
      knownNodesCount: 18,
      signatureSummary: '3-hop automated peeling chain, 80/20 tranche split, sub-minute execution, Binance off-ramp sweep.',
      nodes: {
        root: { label: '🧬 KNOWN FRAUD DNA', sub: 'Campaign #CYB-2048 (Hydra-Peel)' },
        walletA: { name: 'Wallet A', addr: '0xA1b2...9T0', role: 'Victim 1 Hub' },
        walletB: { name: 'Wallet B', addr: '0xB3c4...5D6', role: 'Victim 2 Hub' },
        patternHub: { label: '• Synthesized Fraud Pattern •' },
        candidate: { name: '🆕 Candidate: Wallet Z', addr: '0xAB89C41d2E5F78a9...91F2', match: '91% PATTERN MATCH' }
      },
      dnaReasons: [
        'Similar Transaction Structure: 3-hop peel chain with fan-out into intermediary splitting nodes.',
        'Similar Fund-Splitting Pattern: Exact 80/20 tranche split matching Campaign #CYB-2048 syndicate structure.',
        'Similar Transfer Timing & Cadence: Automated script execution with <45s delay per hop.',
        'Similar Destination Behavior: Consolidation into Binance Hot Cluster 14 gateway.',
        'Connected to Existing Syndicate Wallets: 2nd-degree graph proximity to Wallet A (0xB3c4...5D6) from Case #1245.'
      ],
      vectors: { timing: 94, split: 92, topology: 96, amount: 88, dest: 91, gas: 86 }
    },
    'CYB-3912': {
      id: 'Campaign #CYB-3912',
      name: '"Phantom-Drainer" Phishing DApp Drainer Network',
      shortName: 'Phantom-Drainer Network',
      crimeCategory: 'Malicious Permit2 Phishing Drainer',
      matchPct: 96,
      totalLoss: '₹2,10,00,000+',
      knownNodesCount: 42,
      signatureSummary: 'Sub-15s ERC-20 permit2 drains, cross-chain bridge hopping, relayer gas sponsor.',
      nodes: {
        root: { label: '🧬 KNOWN FRAUD DNA', sub: 'Campaign #CYB-3912 (Phantom-Drainer)' },
        walletA: { name: 'Drainer Alpha', addr: '0x742d...f44e', role: 'Phish Hub 1' },
        walletB: { name: 'Drainer Beta', addr: '0x91a0...44cc', role: 'Phish Hub 2' },
        patternHub: { label: '• Zero-Day Drain Sequence •' },
        candidate: { name: '🆕 Candidate: Wallet Z', addr: '0x3F88E14bD78c90A2...e719', match: '96% PATTERN MATCH' }
      },
      dnaReasons: [
        'Similar Transaction Structure: Instant permit2 multi-token batch drain without victim gas signature.',
        'Similar Fund-Splitting Pattern: 100% immediate swap on Uniswap V3 followed by bridge router dispatch.',
        'Similar Transfer Timing & Cadence: High-velocity execution <12 seconds from victim approval.',
        'Similar Destination Behavior: Cross-chain routing through Across / Stargate Bridge to Tornado Pool.',
        'Connected to Existing Syndicate Wallets: Gas sponsored by shared master relayer dispatcher 0xRelay...99B.'
      ],
      vectors: { timing: 98, split: 95, topology: 92, amount: 94, dest: 99, gas: 97 }
    },
    'CYB-1084': {
      id: 'Campaign #CYB-1084',
      name: '"Golden-Boar" Pig Butchering Investment Syndicate',
      shortName: 'Golden-Boar Syndicate',
      crimeCategory: 'Fake High-Yield Investment Platform',
      matchPct: 88,
      totalLoss: '₹1,45,00,000+',
      knownNodesCount: 29,
      signatureSummary: 'Staged deposit accumulation, 4-tier intermediary fan-out, KuCoin/OKX deposit memo routing.',
      nodes: {
        root: { label: '🧬 KNOWN FRAUD DNA', sub: 'Campaign #CYB-1084 (Golden-Boar)' },
        walletA: { name: 'OTC Dealer 1', addr: '0x8920...43e7', role: 'Victim Intake 1' },
        walletB: { name: 'OTC Dealer 2', addr: '0x44cd...9182', role: 'Victim Intake 2' },
        patternHub: { label: '• Pig Butchering Staging Flow •' },
        candidate: { name: '🆕 Candidate: Wallet Z', addr: '0x98E2F1A034BC588D...8841', match: '88% PATTERN MATCH' }
      },
      dnaReasons: [
        'Similar Transaction Structure: Staged multi-day deposit warming followed by 4-tier intermediary dispersion.',
        'Similar Fund-Splitting Pattern: Equal split tranches into 5 secondary laundering accounts.',
        'Similar Transfer Timing & Cadence: Batched sweeps aligned with Asian market OTC operating hours.',
        'Similar Destination Behavior: Aggregation into KuCoin/OKX Central Deposit Hotwallets with UID memos.',
        'Connected to Existing Syndicate Wallets: Direct UTXO/ERC20 co-spend with syndicate node 0x8920...43e7.'
      ],
      vectors: { timing: 85, split: 89, topology: 91, amount: 87, dest: 90, gas: 84 }
    }
  };

  // Case Profiles Tailored for SIH PS-26183
  const caseProfiles = {
    '0xA1b2C3d4E5f6G7h8I9j0K1L2m3N4o5P6q7R8s9T0': {
      isUnreported: false,
      crimeType: 'Task-Based Telegram Scam (Part-Time Job)',
      received: '₹8,42,000',
      receivedCount: '128 Transactions',
      sent: '₹7,95,000',
      sentCount: '96 Transactions',
      firstActivity: '12 Aug 2026',
      firstTime: '10:24 AM',
      lastActivity: '23 Aug 2026',
      lastTime: '05:42 PM',
      riskScore: 87,
      riskLevel: 'HIGH RISK',
      exchange: 'Binance (Cluster)',
      confidence: '91%',
      caseId: 'CYB-2026-001245',
      fraudDnaMatch: 95,
      matchedCampaignId: 'CYB-2048',
      matchedCampaign: 'Campaign #CYB-2048 ("Hydra-Peel" Telegram Scam)',
      reasons: [
        'Reported by multiple victims via 1930 National Cybercrime Portal',
        'High number of rapid intermediary transfers (peeling chain)',
        'Funds split across 3 intermediary wallets within 12 minutes',
        'Connected to previously flagged task-based syndicate address',
        'Final tranche consolidated into Centralized Exchange deposit gateway'
      ],
      exchangeReasons: [
        'Address matches known exchange multi-sig consolidation patterns',
        'Multiple rapid deposits from distinct victim wallets',
        'Deposit behavior strictly matches Binance internal sweep architecture'
      ],
      dnaReasons: [
        'Similar Transaction Structure: 3-hop peel chain with fan-out into intermediary splitting nodes.',
        'Similar Fund-Splitting Pattern: Exact 80/20 tranche split matching Campaign #CYB-2048 syndicate playbook.',
        'Similar Transfer Timing & Cadence: Automated script execution with <45s delay per hop.',
        'Similar Destination Behavior: Consolidation into Binance Hot Cluster 14 gateway.',
        'Connected to Existing Syndicate Wallets: Root anchor wallet for Campaign #CYB-2048 syndicate.'
      ],
      vectors: { timing: 96, split: 94, dest: 92, topology: 98, amount: 90, gas: 88 },
      hiddenWallets: [
        { addr: '0xB3c4...5D6', fullAddr: '0xB3c4D5e6F7a8B9c0D1E2F3A4B5C6D7E8F9A0B1C2', role: 'Peeling Chain Splitter', roleClass: 'role-splitter', amount: '₹30,000', distance: '1st Degree (Direct Child)', risk: 'High (82)' },
        { addr: '0xFeef...119A', fullAddr: '0x9920FeeF119Ab3408a8c19920199182301938210', role: 'Gas Sponsor Relayer', roleClass: 'role-gas', amount: '₹15,000 Gas', distance: 'Shared Funder (FixedFloat)', risk: 'High (89)' },
        { addr: '0xC7d8...8E9', fullAddr: '0xC7d8E9F0A1B2C3D4E5F678901234567890ABCDEF', role: 'Co-Spending Mule', roleClass: 'role-cospender', amount: '₹18,000', distance: '2nd Degree Hop', risk: 'Medium (65)' },
        { addr: '0xAB89...91F2', fullAddr: '0xAB89C41d2E5F78a9B30C2d4E6F8a91F2', role: 'Fraud DNA Twin (Zero-Day)', roleClass: 'role-dna', amount: '₹1,25,000', distance: '91% DNA Syndicate Link', risk: 'Critical (92)' }
      ],
      txs: [
        { hash: '0x9d8f82a1bc7e44a3b8d91f2c90a1b2c3d4e5f67a1b', shortHash: '0x9d8f...7a1b', from: '0xA1b2...9T0', to: '0xB3c4...5D6', amount: '₹30,000', time: '23 Aug 2026, 05:42 PM', risk: 'High' },
        { hash: '0x4c2e5a7b9c1d3f6e8a0b2c4d6e8f0a2c4e6f3a', shortHash: '0x4c2e...6f3a', from: '0xA1b2...9T0', to: '0xExch...90A (Binance)', amount: '₹20,000', time: '23 Aug 2026, 05:40 PM', risk: 'High' },
        { hash: '0x1a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f2c9d', shortHash: '0x1a7b...2c9d', from: '0xB3c4...5D6', to: '0xC7d8...8E9', amount: '₹18,000', time: '23 Aug 2026, 05:35 PM', risk: 'Medium' },
        { hash: '0x5e3f2a1b4c6d8e0f1a3b5c7d9e1f3a5b7c9d8b7c', shortHash: '0x5e3f...8b7c', from: '0xB3c4...5D6', to: '0xD4e5...2F3', amount: '₹12,000', time: '23 Aug 2026, 05:30 PM', risk: 'Medium' },
        { hash: '0x3b2a1f8c9d0e1a2b3c4d5e6f7a8b9c0d1e2f3a4b', shortHash: '0x3b2a...3a4b', from: 'Victim Wallet', to: '0xA1b2...9T0', amount: '₹50,000', time: '23 Aug 2026, 05:15 PM', risk: 'High' },
        { hash: '0x8f7e6d5c4b3a210987654321fedcba0987654321', shortHash: '0x8f7e...4321', from: '0xA1b2...9T0', to: '0xFeef...119A', amount: '₹15,000', time: '22 Aug 2026, 11:20 AM', risk: 'Medium' }
      ]
    },

    '0x742d35Cc6634C0532925a3b844Bc454e4438f44e': {
      isUnreported: false,
      crimeType: 'Ransomware Extortion Outflow',
      received: '₹34,50,000',
      receivedCount: '412 Transactions',
      sent: '₹34,20,000',
      sentCount: '390 Transactions',
      firstActivity: '04 Jun 2026',
      firstTime: '02:15 PM',
      lastActivity: '24 Aug 2026',
      lastTime: '11:10 AM',
      riskScore: 98,
      riskLevel: 'CRITICAL RISK',
      exchange: 'Tornado Cash Smart Contract',
      confidence: '99%',
      caseId: 'CYB-2026-009812',
      fraudDnaMatch: 96,
      matchedCampaignId: 'CYB-3912',
      matchedCampaign: 'Campaign #CYB-3912 ("Phantom-Drainer" Network)',
      reasons: [
        'Direct connection to OFAC-sanctioned mixer',
        'Peeling chains detected across 40+ tranches',
        'Multiple high-volume zero-knowledge obfuscation calls',
        'Flagged by international anti-money laundering registries',
        'Immediate gas re-funding from known bot clusters'
      ],
      exchangeReasons: [
        'Contract matches Tornado.Cash 100 ETH pool ABI',
        'Zero-knowledge proof verification transactions',
        'Relayer fee settlement addresses detected'
      ],
      dnaReasons: [
        'Similar Transaction Structure: Instant permit2 multi-token batch drain without victim gas signature.',
        'Similar Fund-Splitting Pattern: 100% immediate swap on Uniswap V3 followed by bridge router dispatch.',
        'Similar Transfer Timing & Cadence: High-velocity execution <12 seconds from victim approval.',
        'Similar Destination Behavior: Cross-chain routing through Across / Stargate Bridge to Tornado Pool.',
        'Connected to Existing Syndicate Wallets: Gas sponsored by shared master relayer dispatcher.'
      ],
      vectors: { timing: 98, split: 95, dest: 99, topology: 92, amount: 94, gas: 97 },
      hiddenWallets: [
        { addr: '0xRelay...99B', fullAddr: '0xRelay99B01a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6', role: 'Mixer Relayer Dispatcher', roleClass: 'role-gas', amount: '₹3,40,000', distance: 'Relayer Gas Call', risk: 'Critical (99)' },
        { addr: '0xMixer...49B', fullAddr: '0xMixer49B22cc33dd44ee55ff6677889900112233', role: 'Zero-Knowledge Intermediate', roleClass: 'role-splitter', amount: '₹8,00,000', distance: '1st Degree Pool Call', risk: 'Critical (98)' }
      ],
      txs: [
        { hash: '0xaa11bb22cc33dd44ee55ff667788990011223344', shortHash: '0xaa11...3344', from: '0x742d...f44e', to: 'Tornado.Cash 100ETH', amount: '₹12,50,000', time: '24 Aug 2026, 11:10 AM', risk: 'High' },
        { hash: '0x5566778899aabbccddeeff001122334455667788', shortHash: '0x5566...7788', from: '0x742d...f44e', to: '0xMixer...49B', amount: '₹8,00,000', time: '24 Aug 2026, 09:45 AM', risk: 'High' }
      ]
    },

    '0x89205A3E3b2A69De6Dbf7f01ED13B2108B2c43e7': {
      isUnreported: false,
      crimeType: 'Pig Butchering Investment Scam',
      received: '₹4,15,000',
      receivedCount: '42 Transactions',
      sent: '₹3,90,000',
      sentCount: '38 Transactions',
      firstActivity: '18 Aug 2026',
      firstTime: '08:00 AM',
      lastActivity: '24 Aug 2026',
      lastTime: '01:30 PM',
      riskScore: 74,
      riskLevel: 'HIGH RISK',
      exchange: 'KuCoin Gateway',
      confidence: '84%',
      caseId: 'CYB-2026-003410',
      fraudDnaMatch: 88,
      matchedCampaignId: 'CYB-1084',
      matchedCampaign: 'Campaign #CYB-1084 ("Golden-Boar" Pig Butchering)',
      reasons: [
        'Rapid sweeping after fake high-yield investment deposit',
        'Victim prompted to send funds to unverified OTC dealer',
        'Consolidation within 5 minutes into hot wallet gateway',
        'No prior holding history'
      ],
      exchangeReasons: [
        'Recipient belongs to KuCoin Central Deposit Hotwallet Cluster',
        'Matching internal memo UID routing format',
        'Deposit velocity aligns with known exchange deposit API'
      ],
      dnaReasons: [
        'Similar Transaction Structure: Staged multi-day deposit warming followed by 4-tier intermediary dispersion.',
        'Similar Fund-Splitting Pattern: Equal split tranches into 5 secondary laundering accounts.',
        'Similar Transfer Timing & Cadence: Batched sweeps aligned with Asian market OTC operating hours.',
        'Similar Destination Behavior: Aggregation into KuCoin/OKX Central Deposit Hotwallets with UID memos.',
        'Connected to Existing Syndicate Wallets: Direct UTXO/ERC20 co-spend with syndicate node 0x8920...43e7.'
      ],
      vectors: { timing: 85, split: 89, dest: 90, topology: 91, amount: 87, gas: 84 },
      hiddenWallets: [
        { addr: '0x44cd...9182', fullAddr: '0x44cd9182a1b2c3d4e5f678901234567890abcdef', role: 'Secondary OTC Mule', roleClass: 'role-cospender', amount: '₹1,90,000', distance: '1st Degree Co-Spend', risk: 'High (76)' },
        { addr: '0xKuCoin_Hot2', fullAddr: '0xKuCoinDepositHotwallet02ClusterGateway', role: 'KuCoin UID Aggregator', roleClass: 'role-splitter', amount: '₹2,20,000', distance: 'Final Deposit Hop', risk: 'Medium (68)' }
      ],
      txs: [
        { hash: '0x1234567890abcdef1234567890abcdef12345678', shortHash: '0x1234...5678', from: 'Victim #3', to: '0x8920...43e7', amount: '₹45,000', time: '24 Aug 2026, 01:30 PM', risk: 'High' },
        { hash: '0xfedcba0987654321fedcba0987654321fedcba09', shortHash: '0xfedc...ba09', from: '0x8920...43e7', to: 'KuCoin Hot 2', amount: '₹40,000', time: '24 Aug 2026, 01:45 PM', risk: 'Medium' }
      ]
    },

    '0xAB89C41d2E5F78a9B30C2d4E6F8a91F2': {
      isUnreported: true,
      crimeType: 'Unreported Suspect Address (Zero-Day Ingestion)',
      received: '₹1,25,000',
      receivedCount: '14 Transactions',
      sent: '₹1,20,000',
      sentCount: '12 Transactions',
      firstActivity: '24 Aug 2026',
      firstTime: '02:15 PM',
      lastActivity: '24 Aug 2026',
      lastTime: '06:30 PM',
      riskScore: 92,
      riskLevel: 'CRITICAL RISK',
      exchange: 'Binance (Cluster)',
      confidence: '94%',
      caseId: 'CYB-2026-UNREP-0881',
      fraudDnaMatch: 91,
      matchedCampaignId: 'CYB-2048',
      matchedCampaign: 'Campaign #CYB-2048 ("Hydra-Peel" Telegram Scam)',
      reasons: [
        'Zero prior reports on 1930 portal (Unreported Zero-Day Wallet)',
        '91% Behavioral Fraud DNA match with Campaign #CYB-2048',
        'Immediate 80/20 fund-splitting across 3 intermediary wallets',
        'Automated script execution velocity (<45s per hop)',
        'Final consolidation into Binance Hot Multi-sig Cluster'
      ],
      exchangeReasons: [
        'Sweep delay matches Binance internal consolidation timetable',
        'Deposit memo format identical to Campaign #CYB-2048 deposit patterns',
        'Direct multi-sig signature structure matching Binance hot gateway'
      ],
      dnaReasons: [
        'Similar Transaction Structure: 3-hop peel chain with fan-out into intermediary splitting nodes.',
        'Similar Fund-Splitting Pattern: Exact 80/20 tranche split matching Campaign #CYB-2048 syndicate structure.',
        'Similar Transfer Timing & Cadence: Automated script execution with <45s delay per hop.',
        'Similar Destination Behavior: Consolidation into Binance Hot Cluster 14 gateway.',
        'Connected to Existing Syndicate Wallets: 2nd-degree graph proximity to Wallet A (0xB3c4...5D6) from Case #1245.'
      ],
      vectors: { timing: 94, split: 92, dest: 89, topology: 96, amount: 88, gas: 86 },
      hiddenWallets: [
        { addr: '0xZ_Inter1...44D', fullAddr: '0xZ_Intermediary144D01a2b3c4d5e6f7a8b9c0d1e2', role: 'Tranche Splitter (80%)', roleClass: 'role-splitter', amount: '₹80,000', distance: '1st Degree Direct Child', risk: 'Critical (94)' },
        { addr: '0xZ_Inter2...88E', fullAddr: '0xZ_Intermediary288E01a2b3c4d5e6f7a8b9c0d1e2', role: 'Tranche Splitter (20%)', roleClass: 'role-splitter', amount: '₹20,000', distance: '1st Degree Direct Child', risk: 'High (84)' },
        { addr: '0xB3c4...5D6', fullAddr: '0xB3c4D5e6F7a8B9c0D1E2F3A4B5C6D7E8F9A0B1C2', role: 'Parent Syndicate Node (Case 1245)', roleClass: 'role-dna', amount: '₹50,000', distance: '2nd Degree Shared Lineage', risk: 'High (82)' }
      ],
      txs: [
        { hash: '0x3a91b2c4e5f67a8b9c0d1e2f3a4b5c6d7e8f9a0b', shortHash: '0x3a91...9a0b', from: 'Victim (Unreported)', to: '0xAB89...91F2 (Wallet Z)', amount: '₹1,00,000', time: '24 Aug 2026, 06:15 PM', risk: 'High' },
        { hash: '0x7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f', shortHash: '0x7e8f...5e6f', from: '0xAB89...91F2', to: '0xZ_Inter1...44D', amount: '₹80,000 (80%)', time: '24 Aug 2026, 06:16 PM', risk: 'High' },
        { hash: '0x1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d', shortHash: '0x1c2d...9c0d', from: '0xAB89...91F2', to: '0xZ_Inter2...88E', amount: '₹20,000 (20%)', time: '24 Aug 2026, 06:16 PM', risk: 'High' },
        { hash: '0x9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b', shortHash: '0x9a0b...7a8b', from: '0xZ_Inter1...44D', to: '0xExch...90A (Binance)', amount: '₹78,500', time: '24 Aug 2026, 06:17 PM', risk: 'High' }
      ]
    }
  };

  // --- DYNAMIC FRAUD EVALUATOR FOR ANY ADDRESS ---
  function calculateFraudDNAMatch(address) {
    if (caseProfiles[address]) {
      return caseProfiles[address];
    }
    let hashVal = 0;
    for (let i = 0; i < address.length; i++) {
      hashVal = (hashVal << 5) - hashVal + address.charCodeAt(i);
      hashVal |= 0;
    }
    const absHash = Math.abs(hashVal);
    const campaignKeys = ['CYB-2048', 'CYB-3912', 'CYB-1084'];
    const matchedCampKey = campaignKeys[absHash % campaignKeys.length];
    const camp = campaignDNAProfiles[matchedCampKey];
    const matchPct = 82 + (absHash % 16);

    return {
      isUnreported: true,
      crimeType: `Suspect Address (Attributed: ${camp.crimeCategory})`,
      received: `₹${(45000 + (absHash % 450000)).toLocaleString('en-IN')}`,
      receivedCount: `${18 + (absHash % 60)} Transactions`,
      sent: `₹${(42000 + (absHash % 420000)).toLocaleString('en-IN')}`,
      sentCount: `${14 + (absHash % 50)} Transactions`,
      firstActivity: '15 Aug 2026',
      firstTime: '09:30 AM',
      lastActivity: '24 Aug 2026',
      lastTime: '05:15 PM',
      riskScore: Math.min(99, 78 + (absHash % 20)),
      riskLevel: 'HIGH RISK',
      exchange: absHash % 2 === 0 ? 'Binance (Cluster)' : 'WazirX India Hot',
      confidence: `${86 + (absHash % 12)}%`,
      caseId: `CYB-2026-SCAN-${absHash.toString().slice(-4)}`,
      fraudDnaMatch: matchPct,
      matchedCampaignId: matchedCampKey,
      matchedCampaign: `${camp.id} (${camp.name})`,
      reasons: [
        `Exhibits ${matchPct}% Fraud DNA vector match with ${camp.id}`,
        'Automated multi-hop peeling sequence detected',
        'Rapid fund splitting into intermediary layering nodes',
        'Consolidation pattern aligns with centralized off-ramp sweeps'
      ],
      exchangeReasons: [
        'Multi-deposit convergence matches known exchange gateway profiles',
        'Internal memo UID routing format matches exchange sweep specs'
      ],
      dnaReasons: camp.dnaReasons,
      hiddenWallets: [
        { addr: `0xHop1_${absHash.toString(16).slice(0, 4)}`, fullAddr: `0x${absHash.toString(16)}0001`, role: 'Peeling Intermediary', roleClass: 'role-splitter', amount: '₹35,000', distance: '1st Degree', risk: 'High (80)' },
        { addr: `0xGas_${absHash.toString(16).slice(0, 4)}`, fullAddr: `0x${absHash.toString(16)}0002`, role: 'Gas Funder', roleClass: 'role-gas', amount: '₹10,000', distance: 'Gas Relayer', risk: 'High (85)' }
      ],
      vectors: {
        timing: Math.min(99, camp.vectors.timing - 2 + (absHash % 5)),
        split: Math.min(99, camp.vectors.split - 3 + (absHash % 6)),
        dest: Math.min(99, camp.vectors.dest - 2 + (absHash % 4)),
        topology: camp.vectors.topology,
        amount: camp.vectors.amount,
        gas: camp.vectors.gas
      },
      txs: [
        { hash: `0x${absHash.toString(16)}bc7e44a3b8d91f2c90a1`, shortHash: `0x${absHash.toString(16).slice(0, 4)}...7a1b`, from: 'Victim Inflow', to: address.slice(0, 8) + '...', amount: '₹50,000', time: 'Today, 05:10 PM', risk: 'High' },
        { hash: `0x${(absHash + 1).toString(16)}5a7b9c1d3f6e8a0b2c`, shortHash: `0x${(absHash + 1).toString(16).slice(0, 4)}...6f3a`, from: address.slice(0, 8) + '...', to: 'Intermediary Hop', amount: '₹40,000', time: 'Today, 05:11 PM', risk: 'High' }
      ]
    };
  }

  // --- UI SELECTORS ---
  const pageTitle = document.getElementById('page-title');
  const walletInput = document.getElementById('wallet-input');
  const btnAnalyze = document.getElementById('btn-analyze');
  const btnCopyMain = document.getElementById('btn-copy-main-address');
  const toastContainer = document.getElementById('toast-container');
  const presetBtns = document.querySelectorAll('.preset-btn');

  // Modals
  const modalGraph = document.getElementById('modal-graph');
  const btnViewFullGraph = document.getElementById('btn-view-full-graph');
  const modalPdfDossier = document.getElementById('modal-pdf-dossier');
  const btnDownloadReport = document.getElementById('btn-download-report');
  const pdfPreviewTrigger = document.getElementById('pdf-preview-trigger');
  const btnPrintDossier = document.getElementById('btn-print-dossier');
  const modalPsBrief = document.getElementById('modal-ps-brief');
  const btnOpenPsBrief = document.getElementById('btn-open-ps-brief');
  const modalDnaLineage = document.getElementById('modal-dna-lineage');
  const btnViewDnaLineage = document.getElementById('btn-view-dna-lineage');

  // Navigation Links
  const navLinks = document.querySelectorAll('.nav-link');
  const brandLogoTrigger = document.getElementById('brand-logo-trigger');
  const btnSidebarReport = document.getElementById('btn-sidebar-report');

  // Notification / Profile
  const notifBtn = document.getElementById('notification-btn');
  const notifDropdown = document.getElementById('notification-dropdown');
  const profileChip = document.getElementById('profile-chip');
  const profileDropdown = document.getElementById('profile-dropdown');
  const mobileToggle = document.getElementById('mobile-toggle');
  const sidebar = document.getElementById('sidebar');

  // --- TOAST NOTIFICATIONS ---
  function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type === 'success' ? 'toast-success' : type === 'error' ? 'toast-error' : ''}`;
    
    let iconSvg = `<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>`;
    if (type === 'success') {
      iconSvg = `<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#10b981" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
    }
    
    toast.innerHTML = `${iconSvg} <span>${message}</span>`;
    toastContainer.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(100%)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 3200);
  }

  // --- VIEW ROUTING SYSTEM ---
  function switchView(viewName) {
    state.currentView = viewName;
    
    document.querySelectorAll('.view-content').forEach(view => {
      view.classList.remove('active');
    });

    const targetView = document.getElementById(`view-${viewName}`);
    if (targetView) {
      targetView.classList.add('active');
    }

    navLinks.forEach(link => {
      if (link.dataset.view === viewName) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });

    // Update Core USP step highlights
    document.querySelectorAll('.usp-step').forEach(s => {
      if (s.dataset.view === viewName) {
        s.classList.add('active');
      } else {
        s.classList.remove('active');
      }
    });

    const titles = {
      'dashboard': 'Analyze Suspect Wallet',
      'cross-chain': 'Cross-Chain Bridge & Hop Tracker (TRM Labs)',
      'entities': 'Global Entity & Deanonymization Directory (Arkham)',
      'mixer-demask': 'Mixer & Privacy Demasking Engine (Elliptic)',
      'sanctions': 'OFAC SDN & Global Sanctions Screener',
      'cases': 'Investigator Case Workspace & Evidence Vault',
      'subpoena': 'Automated Section 91 CrPC & MLAT Subpoena Dispatcher',
      'stolen-tracker': 'Stolen Money Tracker — Hop-by-Hop Tranche Following',
      'network-map': 'Fraud Network Map — Cross-Case Crime Syndicate Nexus',
      'safety-check': 'Public Wallet Safety Check — Verify Before Sending Crypto',
      'fraud-dna': 'Fraud DNA™ — Behavioral Campaign Intelligence Matrix',
      'report-fraud': 'Report Crypto Fraud (I4C Intake)',
      'monitor': 'Real-Time Blockchain Monitoring',
      'exchange-intelligence': 'Centralized Exchange Attribution Directory',
      'alerts': 'Live Threat Alerts & Fraud DNA Feed',
      'reports': 'I4C Forensic Dossiers',
      'about': 'SIH 2026 Problem Statement #26183',
      'contact': 'Emergency Forensics Support'
    };
    if (pageTitle) pageTitle.textContent = titles[viewName] || 'CyberTrace Console';

    if (sidebar) sidebar.classList.remove('open');
    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (viewName === 'fraud-dna') {
      renderDnaTree(state.currentCampaignId);
    }
  }

  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const view = link.dataset.view || 'dashboard';
      switchView(view);
    });
  });

  if (brandLogoTrigger) {
    brandLogoTrigger.addEventListener('click', () => switchView('dashboard'));
  }

  if (btnSidebarReport) {
    btnSidebarReport.addEventListener('click', (e) => {
      e.preventDefault();
      switchView('report-fraud');
    });
  }

  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('.nav-trigger');
    if (trigger) {
      e.preventDefault();
      const v = trigger.dataset.view;
      const addrToAnalyze = trigger.dataset.analyze;
      if (v) {
        switchView(v);
        if (addrToAnalyze) {
          updateDashboardData(addrToAnalyze);
        }
      }
    }
  });

  // --- CLIPBOARD HELPER ---
  function copyToClipboard(text, label = 'Address') {
    navigator.clipboard.writeText(text).then(() => {
      showToast(`Copied ${label}: ${text.length > 20 ? text.slice(0, 10) + '...' + text.slice(-6) : text}`, 'success');
    }).catch(() => {
      showToast('Copied to clipboard', 'success');
    });
  }

  document.addEventListener('click', (e) => {
    const copyTarget = e.target.closest('.copyable');
    if (copyTarget && copyTarget.dataset.copy) {
      copyToClipboard(copyTarget.dataset.copy, 'Value');
    }
  });

  if (btnCopyMain) {
    btnCopyMain.addEventListener('click', () => {
      copyToClipboard(walletInput.value, 'Suspect Wallet Address');
    });
  }

  // --- DROPDOWNS ---
  if (notifBtn && notifDropdown) {
    notifBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      notifDropdown.classList.toggle('show');
      profileDropdown.classList.remove('show');
    });
  }

  if (profileChip && profileDropdown) {
    profileChip.addEventListener('click', (e) => {
      e.stopPropagation();
      profileDropdown.classList.toggle('show');
      notifDropdown.classList.remove('show');
    });
  }

  document.addEventListener('click', () => {
    if (notifDropdown) notifDropdown.classList.remove('show');
    if (profileDropdown) profileDropdown.classList.remove('show');
  });

  if (mobileToggle && sidebar) {
    mobileToggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });
  }

  // --- MODAL UTILITIES ---
  function openModal(modalEl) {
    if (modalEl) {
      modalEl.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeModal(modalEl) {
    if (modalEl) {
      modalEl.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  document.querySelectorAll('.modal-backdrop').forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal(modal);
    });

    const closeBtn = modal.querySelector('.btn-close-modal');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => closeModal(modal));
    }
  });

  if (btnOpenPsBrief && modalPsBrief) {
    btnOpenPsBrief.addEventListener('click', () => openModal(modalPsBrief));
  }

  if (btnViewFullGraph && modalGraph) {
    btnViewFullGraph.addEventListener('click', () => {
      const viewport = document.getElementById('graph-full-viewport');
      const flowSvg = document.getElementById('flow-svg');
      if (viewport && flowSvg) {
        viewport.innerHTML = '';
        const clone = flowSvg.cloneNode(true);
        clone.id = 'flow-svg-fullscreen';
        clone.style.width = '100%';
        clone.style.height = '100%';
        viewport.appendChild(clone);
      }
      openModal(modalGraph);
      showToast('Interactive Graph View Opened', 'info');
    });
  }

  if (btnViewDnaLineage && modalDnaLineage) {
    btnViewDnaLineage.addEventListener('click', () => {
      const viewport = document.getElementById('dna-modal-viewport');
      const dnaSvg = document.getElementById('dna-lineage-svg');
      if (viewport && dnaSvg) {
        viewport.innerHTML = '';
        const clone = dnaSvg.cloneNode(true);
        clone.id = 'dna-svg-fullscreen';
        clone.style.width = '100%';
        clone.style.height = '100%';
        viewport.appendChild(clone);
      }
      openModal(modalDnaLineage);
      showToast('Fraud DNA™ Lineage Topology Visualizer Opened', 'info');
    });
  }

  // --- TIME-TRAVEL SCRUBBER PLAYBACK LOGIC ---
  const btnScrubPlay = document.getElementById('btn-scrub-play');
  const btnScrubBack = document.getElementById('btn-scrub-step-back');
  const btnScrubFwd = document.getElementById('btn-scrub-step-fwd');
  const btnScrubSpeed = document.getElementById('btn-scrub-speed');
  const scrubSlider = document.getElementById('flow-timeline-slider');
  const scrubTimeBadge = document.getElementById('scrubber-time-badge');
  const scrubDesc = document.getElementById('scrubber-event-desc');

  const scrubberSteps = [
    { pct: 0, time: 'T+00:00', desc: 'Victim Inflow: ₹50,000 deposited into Suspect Hub' },
    { pct: 33, time: 'T+00:25', desc: 'Step 1/3: 60% (₹30k) split to Layer-1 Splitter Wallet A' },
    { pct: 66, time: 'T+00:26', desc: 'Step 2/3: Layer-2 Fan-Out into Wallet B (₹18k) & Wallet C (₹12k)' },
    { pct: 100, time: 'T+00:27', desc: 'Step 3/3: ₹20k direct sweep to Binance Hot Cluster 14' }
  ];

  function applyScrubberStep(val) {
    if (scrubSlider) scrubSlider.value = val;
    let currentStep = scrubberSteps[0];
    for (let s of scrubberSteps) {
      if (val >= s.pct) currentStep = s;
    }
    if (scrubTimeBadge) scrubTimeBadge.textContent = `${currentStep.time} (${val}% Complete)`;
    if (scrubDesc) scrubDesc.textContent = currentStep.desc;
  }

  if (scrubSlider) {
    scrubSlider.addEventListener('input', (e) => {
      applyScrubberStep(parseInt(e.target.value));
    });
  }

  if (btnScrubPlay) {
    btnScrubPlay.addEventListener('click', () => {
      state.scrubberPlaying = !state.scrubberPlaying;
      if (state.scrubberPlaying) {
        btnScrubPlay.textContent = '❚❚ Pause';
        if (scrubSlider && parseInt(scrubSlider.value) >= 100) scrubSlider.value = 0;
        state.scrubberInterval = setInterval(() => {
          let curr = parseInt(scrubSlider.value) + 5;
          if (curr > 100) {
            curr = 100;
            clearInterval(state.scrubberInterval);
            state.scrubberPlaying = false;
            btnScrubPlay.textContent = '▶ Play';
            showToast('Time-Travel Timeline Playback Completed', 'success');
          }
          applyScrubberStep(curr);
        }, 300 / state.scrubberSpeed);
      } else {
        clearInterval(state.scrubberInterval);
        btnScrubPlay.textContent = '▶ Play';
      }
    });
  }

  if (btnScrubBack) {
    btnScrubBack.addEventListener('click', () => {
      let curr = Math.max(0, parseInt(scrubSlider.value) - 33);
      applyScrubberStep(curr);
    });
  }
  if (btnScrubFwd) {
    btnScrubFwd.addEventListener('click', () => {
      let curr = Math.min(100, parseInt(scrubSlider.value) + 33);
      applyScrubberStep(curr);
    });
  }
  if (btnScrubSpeed) {
    btnScrubSpeed.addEventListener('click', () => {
      state.scrubberSpeed = state.scrubberSpeed === 1 ? 2 : state.scrubberSpeed === 2 ? 4 : 1;
      btnScrubSpeed.textContent = `${state.scrubberSpeed}x`;
      showToast(`Scrubber Playback Speed: ${state.scrubberSpeed}x`, 'info');
    });
  }

  // --- ENTITY DIRECTORY SEARCH ENGINE ---
  const entitySearchInput = document.getElementById('entity-search-input');
  const entityCategorySelect = document.getElementById('entity-category-select');
  const entityTbody = document.getElementById('entity-tbody');

  const globalEntityDB = [
    { name: 'Binance Hot Cluster 14', cat: 'exchange', role: 'CEX Deposit Hotwallet', addr: '0xExch...90A', fullAddr: '0xExch90ABinanceHotCluster14', vol: '₹1,420 Cr (1.2M TXs)', flag: 'Global KYC Compliant', flagRisk: 'low' },
    { name: 'WazirX India Gateway Hot 02', cat: 'exchange', role: 'CEX India FIU Registered', addr: '0xWazirX...Hot02', fullAddr: '0xWazirXIndiaHot02Gateway', vol: '₹280 Cr (410k TXs)', flag: 'FIU-IND Verified', flagRisk: 'low' },
    { name: 'CoinDCX Staging Pool', cat: 'exchange', role: 'CEX Liquidity Cluster', addr: '0xCoinDCX...Pool1', fullAddr: '0xCoinDCXStagingPool01', vol: '₹390 Cr', flag: 'FIU-IND Verified', flagRisk: 'low' },
    { name: 'Lazarus Group (DPRK Syndicate)', cat: 'threat', role: 'State-Sponsored APT Threat', addr: '0x098B...2f96', fullAddr: '0x098B716B8Aaf21512996dC57EB0615e2383E2f96', vol: '₹4,800 Cr Stolen', flag: 'OFAC SDN Sanctioned', flagRisk: 'high' },
    { name: 'LockBit 3.0 Ransomware Vault', cat: 'threat', role: 'Ransomware Extortion Hub', addr: '0xLockBit...33A1', fullAddr: '0xLockBit30RansomwareVault33A1', vol: '₹750 Cr', flag: 'FBI / Europol Seized', flagRisk: 'high' },
    { name: 'Tornado.Cash 100 ETH Pool', cat: 'mixer', role: 'Privacy Mixer Smart Contract', addr: '0x742d...f44e', fullAddr: '0x742d35Cc6634C0532925a3b844Bc454e4438f44e', vol: '₹8,900 Cr Mixed', flag: 'OFAC Sanctioned', flagRisk: 'high' },
    { name: 'Sinbad.io Bitcoin Mixer Relay', cat: 'mixer', role: 'Obfuscation Mixer Node', addr: '0xSinbad...88F1', fullAddr: '0xSinbadMixerRelay88F1', vol: '₹1,200 Cr', flag: 'OFAC Sanctioned', flagRisk: 'high' },
    { name: 'Wintermute Trading OTC Node', cat: 'otc', role: 'Institutional Liquidity', addr: '0xWinter...99E1', fullAddr: '0xWintermuteTradingOTCNode99E1', vol: '₹12,400 Cr', flag: 'Licensed Market Maker', flagRisk: 'low' },
    { name: 'Hydra Market Darknet Hotwallet', cat: 'darknet', role: 'Darknet Marketplace Node', addr: '0xHydra...Clust88', fullAddr: '0xHydraMarketSeizedCluster88', vol: '₹2,100 Cr Seized', flag: 'Seized by BKA / FBI', flagRisk: 'high' }
  ];

  function filterEntityTable() {
    const q = (entitySearchInput?.value || '').toLowerCase();
    const cat = entityCategorySelect?.value || 'all';

    if (!entityTbody) return;
    const filtered = globalEntityDB.filter(e => {
      const matchQ = e.name.toLowerCase().includes(q) || e.fullAddr.toLowerCase().includes(q) || e.role.toLowerCase().includes(q);
      const matchCat = cat === 'all' || e.cat === cat;
      return matchQ && matchCat;
    });

    entityTbody.innerHTML = filtered.map(e => `
      <tr>
        <td><strong>${e.name}</strong></td>
        <td><span class="badge-role ${e.flagRisk === 'high' ? 'role-dna' : 'role-gas'}">${e.role}</span></td>
        <td><span class="font-mono text-cyan copyable" data-copy="${e.fullAddr}">${e.addr}</span></td>
        <td class="font-mono font-bold ${e.flagRisk === 'high' ? 'text-danger' : ''}">${e.vol}</td>
        <td><span class="badge-risk badge-${e.flagRisk}">${e.flag}</span></td>
        <td><button class="btn-ghost-xs btn-trace-entity" data-address="${e.fullAddr}">Trace &rarr;</button></td>
      </tr>
    `).join('');
  }

  if (entitySearchInput) entitySearchInput.addEventListener('input', filterEntityTable);
  if (entityCategorySelect) entityCategorySelect.addEventListener('change', filterEntityTable);

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-trace-entity');
    if (btn && btn.dataset.address) {
      updateDashboardData(btn.dataset.address);
      switchView('dashboard');
      showToast(`Tracing Entity Address: ${btn.dataset.address.slice(0, 12)}...`, 'info');
    }
  });

  // Export Buttons
  const btnExportCross = document.getElementById('btn-export-crosschain-trail');
  if (btnExportCross) {
    btnExportCross.addEventListener('click', () => {
      showToast('Exporting Multi-Chain Bridge Trail Dossier...', 'success');
      loadDossierForAddress(state.currentAddress);
      openModal(modalPdfDossier);
    });
  }

  const btnExportMixer = document.getElementById('btn-export-mixer-dossier');
  if (btnExportMixer) {
    btnExportMixer.addEventListener('click', () => {
      showToast('Exporting Tornado.Cash Zero-Knowledge Demasking Dossier...', 'success');
      loadDossierForAddress('0x742d35Cc6634C0532925a3b844Bc454e4438f44e');
      openModal(modalPdfDossier);
    });
  }

  const btnSaveNotes = document.getElementById('btn-save-case-notes');
  if (btnSaveNotes) {
    btnSaveNotes.addEventListener('click', () => {
      showToast('Investigator Case Notes Saved & Encrypted into Vault!', 'success');
    });
  }

  // Legal Subpoena Tabs
  const btnTabCrpc = document.getElementById('btn-tab-crpc');
  const btnTabCloud = document.getElementById('btn-tab-cloud');
  const btnTabMlat = document.getElementById('btn-tab-mlat');
  const subBox = document.getElementById('subpoena-preview-box');

  if (btnTabCrpc && subBox) {
    btnTabCrpc.addEventListener('click', () => {
      btnTabCrpc.classList.add('active');
      btnTabCloud.classList.remove('active');
      btnTabMlat.classList.remove('active');
      subBox.innerHTML = `
        <h4 class="text-cyan font-bold mb-2">NOTICE UNDER SECTION 91 OF CODE OF CRIMINAL PROCEDURE, 1973</h4>
        <p class="text-xs text-muted mb-2">To: Nodal Law Enforcement Officer, Binance Services / WazirX India / CoinDCX</p>
        <p class="text-xs text-white mb-2"><strong>SUBJECT:</strong> EMERGENCY ORDER TO FREEZE SUSPECT CRYPTOCURRENCY ASSETS IN FIR #CYB-2026-001245</p>
        <p class="text-xs text-secondary leading-relaxed">
          Whereas blockchain intelligence generated by the <strong>CyberTrace Automated Forensics Engine (I4C)</strong> reveals that stolen funds amounting to <strong>₹20,000.00</strong> originating from cyber fraud complaint #1245 were deposited into your Centralized Hot Deposit Gateway (<strong>0xExch...90A</strong>) on <strong>23 Aug 2026, 05:40 PM IST</strong> via TXID: <span class="font-mono text-cyan">0x4c2e5a7b9c1d3f6e8a0b2c4d6e8f0a2c4e6f3a</span>.
          <br/><br/>
          You are hereby commanded under Section 91 CrPC to immediately freeze recipient account and preserve KYC records.
        </p>
      `;
    });
  }

  if (btnTabCloud && subBox) {
    btnTabCloud.addEventListener('click', () => {
      btnTabCloud.classList.add('active');
      btnTabCrpc.classList.remove('active');
      btnTabMlat.classList.remove('active');
      subBox.innerHTML = `
        <h4 class="text-cyan font-bold mb-2">18 U.S.C. § 2703(d) / CLOUD ACT LAW ENFORCEMENT PRESERVATION REQUEST</h4>
        <p class="text-xs text-muted mb-2">To: Global Compliance Desk, Binance Holdings Ltd. / Coinbase Inc.</p>
        <p class="text-xs text-white mb-2"><strong>MATTER:</strong> Transnational Cyber Extortion & Money Laundering Investigation Ref: #CYB-2026-009812</p>
        <p class="text-xs text-secondary leading-relaxed">
          Pursuant to 18 U.S.C. § 2703(f) and international cross-border cyber protocols, you are requested to preserve all records concerning wallet <strong>0x742d...f44e</strong> and destination sweep accounts for 90 days.
        </p>
      `;
    });
  }

  if (btnTabMlat && subBox) {
    btnTabMlat.addEventListener('click', () => {
      btnTabMlat.classList.add('active');
      btnTabCrpc.classList.remove('active');
      btnTabCloud.classList.remove('active');
      subBox.innerHTML = `
        <h4 class="text-cyan font-bold mb-2">MUTUAL LEGAL ASSISTANCE TREATY (MLAT) INTERNATIONAL FREEZE ORDER</h4>
        <p class="text-xs text-muted mb-2">To: Ministry of Justice / Interpol Nodal Contact</p>
        <p class="text-xs text-white mb-2"><strong>CASE:</strong> Multi-Jurisdictional Syndicate Racket #CYB-2048 ("Hydra-Peel")</p>
        <p class="text-xs text-secondary leading-relaxed">
          Formal request under bilateral MLAT provisions to freeze illicit exchange accounts in Singapore, Dubai, and Seychelles linked to ₹84.5 Lakhs in stolen cyber fraud assets.
        </p>
      `;
    });
  }

  const btnDispatchEmail = document.getElementById('btn-dispatch-subpoena-email');
  if (btnDispatchEmail) {
    btnDispatchEmail.addEventListener('click', () => {
      btnDispatchEmail.textContent = 'Dispatching to Binance API...';
      setTimeout(() => {
        btnDispatchEmail.textContent = '⚡ 1-Click Dispatch to Binance Legal Desk';
        showToast('Legal Subpoena Encrypted & Dispatched to Binance Law Enforcement Desk (Case Ref: CYB-2026-001245)', 'success');
      }, 700);
    });
  }

  // Full Fraud Form
  const fullFraudForm = document.getElementById('full-fraud-form');
  if (fullFraudForm) {
    fullFraudForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const suspectAddr = document.getElementById('f-suspect-addr').value;
      const amount = document.getElementById('f-amount').value;
      const scamType = document.getElementById('f-fraud-type').value;

      const newRef = `I4C-${new Date().getFullYear()}-${Math.floor(100000 + Math.random() * 900000)}`;

      state.recentCases.unshift({
        id: newRef,
        target: suspectAddr.length > 14 ? suspectAddr.slice(0, 8) + '...' + suspectAddr.slice(-4) : suspectAddr,
        loss: amount,
        type: scamType || 'Crypto Fraud',
        time: 'Just now',
        status: 'Case Registered'
      });

      renderRecentCasesFeed();
      fullFraudForm.reset();
      showToast(`I4C Case Registered & Traced! Case ID: ${newRef}`, 'success');
    });
  }

  function renderRecentCasesFeed() {
    const feed = document.getElementById('portal-recent-cases');
    if (!feed) return;

    feed.innerHTML = state.recentCases.map(c => `
      <div class="feed-item">
        <div class="flex items-center justify-between">
          <span class="font-mono text-cyan text-xs font-bold">${c.id}</span>
          <span class="badge-risk badge-high">${c.status}</span>
        </div>
        <div class="text-xs text-white">Suspect: <span class="font-mono text-muted">${c.target}</span> &bull; Loss: ${c.loss}</div>
        <div class="text-xs text-muted">${c.type} &bull; ${c.time}</div>
      </div>
    `).join('');
  }
  renderRecentCasesFeed();

  // Load Dossier
  function loadDossierForAddress(address) {
    const profile = calculateFraudDNAMatch(address);
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
      const caseCode = btn.dataset.case;
      const addrMap = {
        'CYB-2026-001245': '0xA1b2C3d4E5f6G7h8I9j0K1L2m3N4o5P6q7R8s9T0',
        'CYB-2026-009812': '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
        'CYB-2026-003410': '0x89205A3E3b2A69De6Dbf7f01ED13B2108B2c43e7',
        'CYB-2026-UNREP-0881': '0xAB89C41d2E5F78a9B30C2d4E6F8a91F2'
      };
      loadDossierForAddress(addrMap[caseCode] || state.currentAddress);
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
  }

  // --- HIDDEN WALLETS RENDERER ---
  function renderHiddenWallets(address) {
    const profile = calculateFraudDNAMatch(address);
    const tbody = document.getElementById('hidden-wallets-tbody');
    const badge = document.getElementById('hidden-wallet-count-badge');
    if (!tbody) return;

    const list = profile.hiddenWallets || [
      { addr: '0xB3c4...5D6', fullAddr: '0xB3c4D5e6F7a8B9c0D1E2F3A4B5C6D7E8F9A0B1C2', role: 'Peeling Splitter', roleClass: 'role-splitter', amount: '₹30,000', distance: '1st Degree', risk: 'High (82)' }
    ];

    if (badge) badge.textContent = `${list.length} Accomplices Found`;

    tbody.innerHTML = list.map(w => `
      <tr>
        <td><span class="font-mono text-white copyable" data-copy="${w.fullAddr}">${w.addr}</span></td>
        <td><span class="badge-role ${w.roleClass}">${w.role}</span></td>
        <td class="font-mono font-semibold">${w.amount}</td>
        <td class="text-xs text-secondary">${w.distance}</td>
        <td><span class="badge-risk ${w.risk.includes('Critical') ? 'badge-high' : w.risk.includes('High') ? 'badge-high' : 'badge-medium'}">${w.risk}</span></td>
        <td><button class="btn-ghost-xs btn-trace-hidden" data-address="${w.fullAddr}">Trace &rarr;</button></td>
      </tr>
    `).join('');
  }

  document.addEventListener('click', (e) => {
    const traceBtn = e.target.closest('.btn-trace-hidden');
    if (traceBtn && traceBtn.dataset.address) {
      updateDashboardData(traceBtn.dataset.address);
      switchView('dashboard');
      showToast(`Now Tracing Discovered Accomplice: ${traceBtn.dataset.address.slice(0, 10)}...`, 'info');
    }
  });

  // --- WALLET ANALYSIS SIMULATION & PRESETS ---
  function updateDashboardData(address) {
    state.currentAddress = address;
    const profile = calculateFraudDNAMatch(address);

    if (walletInput) walletInput.value = address;

    btnAnalyze.innerHTML = `
      <svg class="animate-spin" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="animation: spin 1s linear infinite;"><circle cx="12" cy="12" r="10" stroke-opacity="0.25"></circle><path d="M12 2a10 10 0 0 1 10 10" stroke-linecap="round"></path></svg>
      Scanning...
    `;
    btnAnalyze.disabled = true;

    setTimeout(() => {
      btnAnalyze.innerHTML = 'Analyze';
      btnAnalyze.disabled = false;

      // Update KPIs
      const metricRec = document.getElementById('metric-received');
      const metricRecSub = document.getElementById('metric-received-sub');
      const metricSent = document.getElementById('metric-sent');
      const metricSentSub = document.getElementById('metric-sent-sub');
      const metricFirstD = document.getElementById('metric-first-date');
      const metricFirstT = document.getElementById('metric-first-time');
      const metricLastD = document.getElementById('metric-last-date');
      const metricLastT = document.getElementById('metric-last-time');

      if (metricRec) metricRec.textContent = profile.received;
      if (metricRecSub) metricRecSub.textContent = profile.receivedCount;
      if (metricSent) metricSent.textContent = profile.sent;
      if (metricSentSub) metricSentSub.textContent = profile.sentCount;
      if (metricFirstD) metricFirstD.textContent = profile.firstActivity;
      if (metricFirstT) metricFirstT.textContent = profile.firstTime;
      if (metricLastD) metricLastD.textContent = profile.lastActivity;
      if (metricLastT) metricLastT.textContent = profile.lastTime;

      // Update Risk Gauge
      const scoreVal = document.getElementById('risk-score-val');
      const levelTag = document.getElementById('risk-level-tag');
      const gaugeProgress = document.getElementById('gauge-progress');
      if (scoreVal) scoreVal.textContent = profile.riskScore;
      if (levelTag) levelTag.textContent = profile.riskLevel;

      if (gaugeProgress) {
        const offset = 188.5 * (1 - profile.riskScore / 100);
        gaugeProgress.style.strokeDashoffset = offset;
      }

      // Update Suspicion Checklist
      const suspList = document.getElementById('suspicion-list');
      if (suspList && profile.reasons) {
        suspList.innerHTML = profile.reasons.map(r => `
          <li class="suspicion-item">
            <span class="check-icon red-check">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="9" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444"/><polyline points="8 12 11 15 16 9" stroke="#ef4444"></polyline></svg>
            </span>
            <span class="check-text">${r}</span>
          </li>
        `).join('');
      }

      // Update Fraud DNA Card
      const dnaBannerTitle = document.getElementById('dna-banner-title');
      const dnaCardWallet = document.getElementById('dna-card-wallet');
      const dnaCardMatch = document.getElementById('dna-card-match');
      const dnaCardCampaign = document.getElementById('dna-card-campaign');
      const dnaReasonsList = document.getElementById('dna-indicators-list');
      const vecTiming = document.getElementById('vec-timing');
      const vecTimingBar = document.getElementById('vec-timing-bar');
      const vecSplit = document.getElementById('vec-split');
      const vecSplitBar = document.getElementById('vec-split-bar');
      const vecDest = document.getElementById('vec-dest');
      const vecDestBar = document.getElementById('vec-dest-bar');

      const shortAddr = address.length > 16 ? `${address.slice(0, 6)}...${address.slice(-4)}` : address;

      if (dnaBannerTitle) {
        dnaBannerTitle.innerHTML = profile.isUnreported
          ? `🔴 Potential Unreported Fraud Wallet Detected`
          : `🧬 Known Fraud Syndicate Fingerprint Match`;
      }
      if (dnaCardWallet) dnaCardWallet.textContent = shortAddr;
      if (dnaCardMatch) dnaCardMatch.textContent = `${profile.fraudDnaMatch || 91}% Pattern Match`;
      if (dnaCardCampaign) dnaCardCampaign.textContent = profile.matchedCampaign || 'Campaign #CYB-2048 ("Hydra-Peel" Telegram Scam)';

      if (dnaReasonsList && profile.dnaReasons) {
        dnaReasonsList.innerHTML = profile.dnaReasons.map(r => {
          const parts = r.split(':');
          const title = parts.length > 1 ? parts[0] : 'Behavioral Marker';
          const desc = parts.length > 1 ? parts.slice(1).join(':') : r;
          return `
            <li class="dna-item">
              <span class="dna-bullet-icon">🧬</span>
              <div class="dna-item-content">
                <strong>${title}</strong>
                <p>${desc}</p>
              </div>
            </li>
          `;
        }).join('');
      }

      if (profile.vectors) {
        if (vecTiming) vecTiming.textContent = `${profile.vectors.timing}%`;
        if (vecTimingBar) vecTimingBar.style.width = `${profile.vectors.timing}%`;
        if (vecSplit) vecSplit.textContent = `${profile.vectors.split}%`;
        if (vecSplitBar) vecSplitBar.style.width = `${profile.vectors.split}%`;
        if (vecDest) vecDest.textContent = `${profile.vectors.dest}%`;
        if (vecDestBar) vecDestBar.style.width = `${profile.vectors.dest}%`;
      }

      // Update Exchange Attribution
      const exchName = document.getElementById('exchange-name');
      const confVal = document.getElementById('confidence-val');
      const exchReasons = document.getElementById('exchange-reasons-list');
      if (exchName) exchName.textContent = profile.exchange;
      if (confVal) confVal.textContent = profile.confidence;
      if (exchReasons && profile.exchangeReasons) {
        exchReasons.innerHTML = profile.exchangeReasons.map(r => `<li>${r}</li>`).join('');
      }

      // Update Case ID
      const cardCaseId = document.getElementById('card-case-id');
      if (cardCaseId) cardCaseId.textContent = `Case ID: ${profile.caseId}`;

      // Render Recent Tx table & Hidden Wallets
      renderRecentTransactionsTable(profile.txs);
      renderHiddenWallets(address);

      if (profile.isUnreported) {
        showToast(`🔴 Fraud DNA Alert: Unreported Wallet ${shortAddr} matched to ${profile.matchedCampaign} (${profile.fraudDnaMatch}%)`, 'error');
      } else {
        showToast(`PS-26183 Exchange Attribution & Fraud DNA: ${profile.exchange} (${profile.confidence})`, 'success');
      }
    }, 400);
  }

  function renderRecentTransactionsTable(txs) {
    const tbody = document.getElementById('tx-tbody');
    if (!tbody) return;
    tbody.innerHTML = '';

    (txs || []).slice(0, 4).forEach(tx => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><span class="font-mono clickable-cell copyable" data-copy="${tx.hash}">${tx.shortHash}</span></td>
        <td><span class="font-mono text-muted copyable" data-copy="${tx.from}">${tx.from}</span></td>
        <td><span class="font-mono text-muted copyable" data-copy="${tx.to}">${tx.to}</span></td>
        <td class="font-mono font-semibold">${tx.amount}</td>
        <td class="text-secondary font-mono">${tx.time}</td>
        <td><span class="badge-risk badge-${tx.risk.toLowerCase()}">${tx.risk}</span></td>
      `;
      tbody.appendChild(tr);
    });
  }
  renderRecentTransactionsTable(caseProfiles['0xA1b2C3d4E5f6G7h8I9j0K1L2m3N4o5P6q7R8s9T0'].txs);
  renderHiddenWallets('0xA1b2C3d4E5f6G7h8I9j0K1L2m3N4o5P6q7R8s9T0');

  if (btnAnalyze) {
    btnAnalyze.addEventListener('click', () => {
      const val = walletInput.value.trim();
      if (!val) {
        showToast('Please enter a valid wallet address', 'error');
        return;
      }
      updateDashboardData(val);
    });
  }

  presetBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      presetBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const addr = btn.dataset.address;
      if (addr) updateDashboardData(addr);
    });
  });

  // SVG node clicks in flow graph
  const nodes = document.querySelectorAll('.graph-node');
  nodes.forEach(node => {
    node.addEventListener('click', () => {
      const title = node.querySelector('.node-title')?.textContent || 'Node';
      const detail = node.querySelector('.font-mono')?.textContent || '';
      showToast(`Selected Node: ${title} (${detail})`, 'info');
    });
  });

  // --- DYNAMIC FRAUD DNA TREE RENDERER ---
  function renderDnaTree(campaignId) {
    state.currentCampaignId = campaignId;
    const camp = campaignDNAProfiles[campaignId] || campaignDNAProfiles['CYB-2048'];
    const svg = document.getElementById('dna-lineage-svg');
    if (!svg) return;

    document.querySelectorAll('.campaign-card').forEach(c => {
      if (c.dataset.campaign === campaignId) {
        c.classList.add('active');
      } else {
        c.classList.remove('active');
      }
    });

    const rootNode = document.getElementById('node-root-dna');
    const walletANode = document.getElementById('node-wallet-a-dna');
    const walletBNode = document.getElementById('node-wallet-b-dna');
    const patternNode = document.getElementById('node-pattern-hub');
    const walletZNode = document.getElementById('node-wallet-z-dna');

    if (rootNode) {
      rootNode.querySelector('text:first-of-type').textContent = camp.nodes.root.label;
      rootNode.querySelector('text:last-of-type').textContent = camp.nodes.root.sub;
    }
    if (walletANode) {
      const texts = walletANode.querySelectorAll('text');
      if (texts[0]) texts[0].textContent = camp.nodes.walletA.name;
      if (texts[1]) texts[1].textContent = camp.nodes.walletA.addr;
      if (texts[2]) texts[2].textContent = camp.nodes.walletA.role;
    }
    if (walletBNode) {
      const texts = walletBNode.querySelectorAll('text');
      if (texts[0]) texts[0].textContent = camp.nodes.walletB.name;
      if (texts[1]) texts[1].textContent = camp.nodes.walletB.addr;
      if (texts[2]) texts[2].textContent = camp.nodes.walletB.role;
    }
    if (patternNode) {
      patternNode.querySelector('text').textContent = camp.nodes.patternHub.label;
    }
    if (walletZNode) {
      const texts = walletZNode.querySelectorAll('text');
      if (texts[0]) texts[0].textContent = camp.nodes.candidate.name;
      if (texts[1]) texts[1].textContent = camp.nodes.candidate.addr;
      if (texts[2]) texts[2].textContent = camp.nodes.candidate.match;
    }
  }

  document.querySelectorAll('.campaign-card').forEach(card => {
    card.addEventListener('click', () => {
      const campKey = card.dataset.campaign;
      if (campKey) {
        renderDnaTree(campKey);
        showToast(`Fraud DNA Matrix switched to ${campaignDNAProfiles[campKey].name}`, 'info');
      }
    });
  });

  const btnRefreshDnaTree = document.getElementById('btn-refresh-dna-tree');
  if (btnRefreshDnaTree) {
    btnRefreshDnaTree.addEventListener('click', () => {
      btnRefreshDnaTree.innerHTML = '&#8635; Computing Vector Centroids...';
      setTimeout(() => {
        btnRefreshDnaTree.innerHTML = '&#8635; Re-run Vector Model';
        renderDnaTree(state.currentCampaignId);
        showToast('Fraud DNA Vector Centroid calculations refreshed across 3 Active Syndicates', 'success');
      }, 600);
    });
  }

  const btnDnaApplyDashboard = document.getElementById('btn-dna-apply-dashboard');
  if (btnDnaApplyDashboard) {
    btnDnaApplyDashboard.addEventListener('click', () => {
      switchView('dashboard');
      updateDashboardData('0xAB89C41d2E5F78a9B30C2d4E6F8a91F2');
    });
  }

  // --- STOLEN MONEY TRACKER TRANCHE LOGIC ---
  document.querySelectorAll('.tranche-card').forEach(tc => {
    tc.addEventListener('click', () => {
      document.querySelectorAll('.tranche-card').forEach(c => c.classList.remove('active'));
      tc.classList.add('active');
      const txid = tc.dataset.txid;
      showToast(`Stolen Money Tracker switched to ${txid === 'tx-100k' ? '₹1,00,000 Tranche (Wallet Z)' : '₹50,000 Tranche (Case 1245)'}`, 'info');
    });
  });

  const btnExportStolenTrail = document.getElementById('btn-export-stolen-trail');
  if (btnExportStolenTrail) {
    btnExportStolenTrail.addEventListener('click', () => {
      const csv = `Hop,Role,Amount_INR,Percentage,From_Address,To_Address,Timestamp,TXID\n0,Victim Ingestion,50000,100%,Victim_Account,0xA1b2C3d4E5f6G7h8I9j0K1L2m3N4o5P6q7R8s9T0,2026-08-23 17:15:22,0x3b2a3a4b\n1A,Peeling Split 1,30000,60%,0xA1b2...9T0,0xB3c4D5e6F7a8B9c0D1E2F3A4B5C6D7E8F9A0B1C2,2026-08-23 17:42:00,0x9d8f7a1b\n1B,CEX Deposit 1,20000,40%,0xA1b2...9T0,0xExch90ABinanceHotCluster14,2026-08-23 17:40:00,0x4c2e6f3a\n2A,Layer 2 Fanout,18000,36%,0xB3c4...5D6,0xC7d8WazirXGateway,2026-08-23 17:35:10,0x1a7b2c9d\n2B,Layer 2 Fanout,12000,24%,0xB3c4...5D6,0xD4e5IntermediateHold,2026-08-23 17:30:00,0x5e3f8b7c`;
      const blob = new Blob([csv], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `stolen_money_trail_${state.caseId}.csv`;
      a.click();
      showToast('Stolen Money Trail CSV Exported!', 'success');
    });
  }

  // --- PUBLIC WALLET SAFETY CHECK ENGINE ---
  const safetyInput = document.getElementById('safety-wallet-input');
  const btnRunSafety = document.getElementById('btn-run-safety-check');
  const safetyVerdictCard = document.getElementById('safety-verdict-card');
  const safetyTitle = document.getElementById('safety-verdict-title');
  const safetySub = document.getElementById('safety-verdict-sub');

  function runPublicSafetyCheck(address) {
    const addr = (address || '').trim();
    if (!addr) return;
    if (safetyInput) safetyInput.value = addr;

    if (addr.toLowerCase().includes('388c') || addr.toLowerCase().includes('coinbase')) {
      if (safetyVerdictCard) safetyVerdictCard.className = 'card safety-verdict-card safe-verdict';
      if (safetyTitle) safetyTitle.textContent = '✅ VERIFIED SAFE / EXCHANGE COLD VAULT';
      if (safetySub) safetySub.textContent = 'Known institutional reserve with zero cybercrime incident reports';
      const sf1 = document.getElementById('safe-f1');
      const sf2 = document.getElementById('safe-f2');
      const sf3 = document.getElementById('safe-f3');
      const sf4 = document.getElementById('safe-f4');
      if (sf1) sf1.textContent = '0 Reports across 1930 and state cyber cells.';
      if (sf2) sf2.textContent = '0% match to known crime syndicates.';
      if (sf3) sf3.textContent = 'Regular long-term holding; no laundering sweeps.';
      if (sf4) sf4.textContent = 'Clean on all global anti-money laundering registries.';
      showToast('Public Safety Verdict: Address is SAFE & Verified', 'success');
    } else if (addr === '0xAB89C41d2E5F78a9B30C2d4E6F8a91F2') {
      if (safetyVerdictCard) safetyVerdictCard.className = 'card safety-verdict-card danger-verdict';
      if (safetyTitle) safetyTitle.textContent = '🔴 DO NOT SEND — ZERO-DAY FRAUD DNA DETECTED';
      if (safetySub) safetySub.textContent = 'Zero prior police reports, but 91% match to Telegram Scam Syndicate #CYB-2048';
      const sf1 = document.getElementById('safe-f1');
      const sf2 = document.getElementById('safe-f2');
      const sf3 = document.getElementById('safe-f3');
      const sf4 = document.getElementById('safe-f4');
      if (sf1) sf1.textContent = 'Unreported on 1930 (Zero-Day Attack Pattern)';
      if (sf2) sf2.textContent = '91% Match to Campaign #CYB-2048 ("Hydra-Peel")';
      if (sf3) sf3.textContent = 'Automated peeling script with <45s hop cadence';
      if (sf4) sf4.textContent = 'Funds routed to Binance Multi-sig sweep cluster';
      showToast('Public Safety Verdict: 🔴 DANGER — Unreported Fraud DNA Detected', 'error');
    } else {
      if (safetyVerdictCard) safetyVerdictCard.className = 'card safety-verdict-card danger-verdict';
      if (safetyTitle) safetyTitle.textContent = '⛔ DO NOT SEND FUNDS — HIGH RISK SCAM';
      if (safetySub) safetySub.textContent = 'Reported in multiple active cybercrime complaints on 1930 portal';
      const sf1 = document.getElementById('safe-f1');
      const sf2 = document.getElementById('safe-f2');
      const sf3 = document.getElementById('safe-f3');
      const sf4 = document.getElementById('safe-f4');
      if (sf1) sf1.textContent = 'Reported by 14 victims in Telegram task fraud cases.';
      if (sf2) sf2.textContent = '95% match to Campaign #CYB-2048 ("Hydra-Peel" syndicate).';
      if (sf3) sf3.textContent = 'Funds swept to intermediary wallets within 45 seconds of receipt.';
      if (sf4) sf4.textContent = 'Flagged in Chainalysis, TRM Labs, and FIU-IND alerts.';
      showToast('Public Safety Verdict: ⛔ HIGH RISK SCAM — Do NOT transfer funds', 'error');
    }
  }

  if (btnRunSafety) {
    btnRunSafety.addEventListener('click', () => {
      runPublicSafetyCheck(safetyInput.value);
    });
  }

  document.querySelectorAll('[data-test-addr]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('[data-test-addr]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      runPublicSafetyCheck(btn.dataset.testAddr);
    });
  });

  // --- JUDGES DEMO BAR STEP-BY-STEP TOUR ---
  const demoButtons = document.querySelectorAll('.btn-demo-step');
  demoButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const step = parseInt(btn.dataset.step);
      demoButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      document.querySelectorAll('.highlight-step').forEach(el => el.classList.remove('highlight-step'));
      switchView('dashboard');

      if (step === 1) {
        const searchSec = document.getElementById('section-search');
        if (searchSec) {
          searchSec.classList.add('highlight-step');
          searchSec.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        if (walletInput) walletInput.focus();
        showToast('Demo Step 1: Suspect Wallet address entered', 'info');
      } else if (step === 2) {
        if (btnAnalyze) btnAnalyze.click();
        showToast('Demo Step 2: Automated blockchain analytics scan triggered', 'info');
      } else if (step === 3) {
        const riskSec = document.getElementById('section-risk');
        if (riskSec) {
          riskSec.classList.add('highlight-step');
          riskSec.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        showToast('Demo Step 3: Heuristic AI Risk Score & Crime Factors identified', 'info');
      } else if (step === 4) {
        const flowSec = document.getElementById('section-flow');
        if (flowSec) {
          flowSec.classList.add('highlight-step');
          flowSec.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        showToast('Demo Step 4: Multi-hop transaction flow graph visualized', 'info');
      } else if (step === 5) {
        const destSec = document.getElementById('section-destination');
        if (destSec) {
          destSec.classList.add('highlight-step');
          destSec.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        showToast('Demo Step 5: Centralized Exchange (Binance Cluster) 91% identified', 'info');
      } else if (step === 6) {
        const dnaSec = document.getElementById('section-fraud-dna');
        updateDashboardData('0xAB89C41d2E5F78a9B30C2d4E6F8a91F2');
        if (dnaSec) {
          dnaSec.classList.add('highlight-step');
          dnaSec.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        showToast('Demo Step 6: 🔴 Zero-Day Fraud DNA Match Detected (91% Match with Campaign #CYB-2048)', 'error');
      } else if (step === 7) {
        const repSec = document.getElementById('section-report');
        if (repSec) {
          repSec.classList.add('highlight-step');
          repSec.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        loadDossierForAddress(state.currentAddress);
        openModal(modalPdfDossier);
        showToast('Demo Step 7: I4C Section 91 CrPC compliant investigation dossier generated with Fraud DNA Findings', 'success');
      }
    });
  });

  // --- REAL-TIME MONITORING STREAM SIMULATOR ---
  const liveMonitorTbody = document.getElementById('live-monitor-tbody');
  const btnToggleLive = document.getElementById('btn-toggle-live-feed');
  const liveStatusText = document.getElementById('live-feed-status');

  const simulatedStreams = [
    { hash: '0x3c2a...881f', target: '0xAB89...91F2 (Wallet Z)', counter: 'Binance Hot 14', amount: '₹80,000', time: '1s ago', threat: 'Fraud DNA (91%)' },
    { hash: '0x9d8f...7a1b', target: '0xA1b2...9T0 (Hub)', counter: 'Binance Hot 14', amount: '₹20,000', time: '4s ago', threat: 'High (87)' },
    { hash: '0x992e...44b1', target: '0xB3c4...5D6 (Split)', counter: 'WazirX India Hot', amount: '₹12,000', time: '8s ago', threat: 'Medium (65)' },
    { hash: '0x7711...aa90', target: '0x742d...f44e (Mixer)', counter: 'Tornado.Cash 10ETH', amount: '₹1,20,000', time: '12s ago', threat: 'High (98)' },
    { hash: '0x55aa...11cc', target: '0x8920...43e7 (Drain)', counter: 'KuCoin Gateway 2', amount: '₹35,000', time: '18s ago', threat: 'High (74)' }
  ];

  function renderInitialLiveStream() {
    if (!liveMonitorTbody) return;
    liveMonitorTbody.innerHTML = simulatedStreams.map(ev => `
      <tr>
        <td><span class="live-pulse"></span> <span class="text-xs text-muted">Ingested</span></td>
        <td><span class="font-mono text-cyan copyable" data-copy="${ev.hash}">${ev.hash}</span></td>
        <td><span class="font-mono text-white">${ev.target}</span></td>
        <td><span class="font-mono text-muted">${ev.counter}</span></td>
        <td class="font-mono font-semibold">${ev.amount}</td>
        <td class="font-mono text-muted">${ev.time}</td>
        <td><span class="badge-risk ${ev.threat.includes('DNA') || ev.threat.includes('High') ? 'badge-high' : 'badge-medium'}">${ev.threat}</span></td>
      </tr>
    `).join('');
  }
  renderInitialLiveStream();

  function startLiveStream() {
    if (state.liveInterval) clearInterval(state.liveInterval);
    state.liveInterval = setInterval(() => {
      if (!liveMonitorTbody) return;
      const randomAmounts = ['₹8,500', '₹22,000', '₹80,000', '₹18,200', '₹50,000'];
      const randomTargs = ['0xAB89...91F2 (Wallet Z)', '0xA1b2...9T0 (Hub)', '0xB3c4...5D6 (Split)', '0x742d...f44e (Mixer)'];
      const randomCounters = ['Binance Cluster', 'WazirX India Gateway', 'OKX Deposit Cluster', 'CoinDCX Hot Wallet'];

      const newRow = document.createElement('tr');
      newRow.style.backgroundColor = 'rgba(139, 92, 246, 0.12)';
      newRow.innerHTML = `
        <td><span class="live-pulse"></span> <span class="text-xs text-cyan">Live Event</span></td>
        <td><span class="font-mono text-cyan copyable" data-copy="0x${Math.random().toString(16).slice(2, 10)}...${Math.random().toString(16).slice(2, 6)}">0x${Math.random().toString(16).slice(2, 6)}...${Math.random().toString(16).slice(2, 6)}</span></td>
        <td><span class="font-mono text-white">${randomTargs[Math.floor(Math.random() * randomTargs.length)]}</span></td>
        <td><span class="font-mono text-muted">${randomCounters[Math.floor(Math.random() * randomCounters.length)]}</span></td>
        <td class="font-mono font-semibold">${randomAmounts[Math.floor(Math.random() * randomAmounts.length)]}</td>
        <td class="font-mono text-muted">Just now</td>
        <td><span class="badge-risk badge-high">DNA Match (91%)</span></td>
      `;

      liveMonitorTbody.insertBefore(newRow, liveMonitorTbody.firstChild);
      setTimeout(() => {
        newRow.style.backgroundColor = '';
        newRow.style.transition = 'background-color 1s ease';
      }, 1500);

      if (liveMonitorTbody.children.length > 20) {
        liveMonitorTbody.removeChild(liveMonitorTbody.lastChild);
      }
    }, 4500);
  }
  startLiveStream();

  if (btnToggleLive) {
    btnToggleLive.addEventListener('click', () => {
      state.isLiveMonitoring = !state.isLiveMonitoring;
      if (state.isLiveMonitoring) {
        startLiveStream();
        if (liveStatusText) liveStatusText.textContent = 'Live Stream Active';
        showToast('Real-time blockchain monitoring resumed', 'info');
      } else {
        clearInterval(state.liveInterval);
        if (liveStatusText) liveStatusText.textContent = 'Stream Paused';
        showToast('Real-time blockchain monitoring paused', 'info');
      }
    });
  }

  // Contact form
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      contactForm.reset();
      showToast('Emergency Forensics Inquiry Transmitted to I4C Duty Desk', 'success');
    });
  }

  // Sync exchange heuristics
  const btnSyncExch = document.getElementById('btn-sync-exchange-heuristics');
  if (btnSyncExch) {
    btnSyncExch.addEventListener('click', () => {
      btnSyncExch.textContent = 'Syncing Heuristics...';
      setTimeout(() => {
        btnSyncExch.innerHTML = '&#8635; Refresh Heuristics Engine';
        showToast('Exchange Cluster Heuristics Updated across 42 Exchanges', 'success');
      }, 800);
    });
  }
});
