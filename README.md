# SecOps

ホームラボで取り組んでいるセキュリティ運用（SOC・ブルーチーム）の学習プロジェクト集。VirtualBox上のKali Linux、Ubuntu Server、Windows 11ホストで検証環境を構築し、Splunk Enterpriseでログの収集・検知・調査を行っている。`ssh-bruteforce-detection-lab/` と `incident-response-case-study/` は、Linuxの認証ログからSSHブルートフォースを検知し、インシデントとして調査・報告するプロジェクト。`windows-event-monitoring/` は、SysmonとSplunk Universal Forwarderを使ってWindowsエンドポイントのテレメトリをSplunkに集約するプロジェクト。各フォルダは独立したプロジェクトで、構成・手順・SPL検索はそれぞれのREADMEにまとめている。

Security operations (SOC / blue team) projects from a home lab. Kali Linux, Ubuntu Server and a Windows 11 host run on VirtualBox, with Splunk Enterprise collecting, detecting and investigating the logs. `ssh-bruteforce-detection-lab/` and `incident-response-case-study/` detect SSH brute-force activity in Linux authentication logs, then investigate and report it as an incident. `windows-event-monitoring/` centralizes Windows endpoint telemetry in Splunk with Sysmon and the Splunk Universal Forwarder. Each folder is a separate project; its README covers the setup, steps and SPL searches.

| フォルダ / Folder | 内容 / Focus | ツール / Tools |
|---|---|---|
| [`ssh-bruteforce-detection-lab/`](ssh-bruteforce-detection-lab/) | SSHブルートフォースの検知 / Detecting SSH brute-force attempts | Kali Linux + Ubuntu Server + OpenSSH + Splunk Enterprise |
| [`incident-response-case-study/`](incident-response-case-study/) | インシデントの調査・報告 / Investigating and reporting the incident | Splunk Enterprise + `auth.log` |
| [`windows-event-monitoring/`](windows-event-monitoring/) | Windowsエンドポイント監視 / Windows endpoint monitoring | Sysmon + Splunk Universal Forwarder + Splunk Enterprise |
| [`vulnerability-assessment-lab/`](vulnerability-assessment-lab/) | 脆弱性評価（準備中） / Vulnerability assessment (in progress) | — |

すべての検証は、外部ネットワークから隔離したホストオンリーネットワーク内で実施している。

All testing runs on an isolated VirtualBox host-only network.
