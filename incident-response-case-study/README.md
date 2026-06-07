Lab Architecture / ラボのアーキテクチャ

Windows 11 Host / Windows 11 ホスト
│
├── Kali Linux VM / Kali Linux 仮想マシン
│   └── Attacker Machine / 攻撃用マシン
│
└── Ubuntu Server VM / Ubuntu Server 仮想マシン
    ├── SSH Target Server / SSHターゲットサーバー
    └── Splunk Enterprise Free / Splunk Enterprise Free（ログ分析・SIEM）