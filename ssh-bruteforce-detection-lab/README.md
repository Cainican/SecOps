# SSH Brute-Force Detection Lab

This project demonstrates the detection of SSH brute-force attacks using Splunk SIEM in a home cybersecurity lab environment.

Attack traffic was generated from Kali Linux against an Ubuntu Server target. Authentication logs were then forwarded to Splunk for analysis, alert creation, and dashboard visualization.

```text
Kali Linux → Ubuntu Server → Splunk
    attack       logs       detection
```

---

# SSH ブルートフォース攻撃検知ラボ

このプロジェクトでは、ホームサイバーセキュリティラボ環境において、
Splunk SIEM を使用した SSH ブルートフォース攻撃の検知を実演しています。

Kali Linux から Ubuntu Server に対して攻撃トラフィックを生成し、
認証ログを Splunk に転送して分析・アラート作成・ダッシュボード可視化を行いました。

```text
Kali Linux → Ubuntu Server → Splunk
    攻撃         ログ         検知
```

---

# Technologies Used

## 使用技術

* Kali Linux
* Ubuntu Server
* Splunk Enterprise
* OpenSSH
* Hydra
* Linux Syslogs
* VirtualBox / VMware

---

# Lab Architecture

| Role             | System                |
| ---------------- | --------------------- |
| Attacker Machine | Kali Linux            |
| Target Server    | Ubuntu Server         |
| SIEM Platform    | Splunk Enterprise     |
| Attack Method    | Hydra SSH Brute Force |
| Log Source       | `/var/log/auth.log`   |

## ラボ構成

| 役割                | システム                  |
| -----------------  | ------------------------- |
| 攻撃マシン          | Kali Linux                |
| 対象サーバ          | Ubuntu Server             |
| SIEMプラットフォーム | Splunk Enterprise         |
| 攻撃手法            | Hydra SSH ブルートフォース  |
| ログソース          | `/var/log/auth.log`       |

---

# Objectives

* Simulate SSH brute-force attacks in a safe lab environment
* Forward Linux authentication logs to Splunk
* Detect failed SSH login attempts
* Analyze attack behavior using SIEM tools
* Create basic alerting and visualization dashboards

## 目的

* 安全なラボ環境で SSH ブルートフォース攻撃を再現
* Linux 認証ログを Splunk に転送
* SSH ログイン失敗を検知
* SIEM ツールを用いて攻撃挙動を分析
* 基本的なアラートとダッシュボードを作成

---

# Attack Simulation

## 攻撃シミュレーション

Hydra was used from the Kali Linux machine to simulate multiple failed SSH login attempts against the Ubuntu Server target.

Kali Linux マシンから Hydra を使用し、Ubuntu Server に対して複数回の SSH ログイン失敗攻撃をシミュレーションしました。

### Example attack command

### 攻撃コマンド例

```bash
hydra -l root -P rockyou.txt ssh://TARGET_IP
```

---

# Log Analysis

## ログ分析

Authentication logs were monitored and forwarded into Splunk for analysis.

認証ログを監視し、Splunk に転送して分析を行いました。

### Example Linux authentication log

### Linux認証ログ例

```text
Failed password for invalid user admin from 192.168.x.x port 22 ssh2
```

### Example Splunk search query

### Splunk検索クエリ例

```spl
index=linux sourcetype=syslog "Failed password"
| stats count by src_ip
| sort - count
```

---

# Detection Workflow

1. Configure SSH service on Ubuntu Server
2. Generate brute-force traffic using Hydra
3. Collect authentication logs from `/var/log/auth.log`
4. Forward logs into Splunk
5. Search and analyze failed login attempts
6. Create dashboards and alerts for detection

## 検知フロー

1. Ubuntu Server の SSH サービスを設定
2. Hydra を使用してブルートフォース攻撃を実行
3. `/var/log/auth.log` から認証ログを収集
4. ログを Splunk に転送
5. ログイン失敗イベントを検索・分析
6. ダッシュボードとアラートを作成

---

# Skills Demonstrated

* SIEM Monitoring
* Splunk Search Processing Language (SPL)
* Linux Administration
* SSH Security Monitoring
* Log Analysis
* Threat Detection
* Blue Team Operations
* Cybersecurity Lab Development

## 習得・実践したスキル

* SIEM監視
* Splunk SPL検索
* Linuxサーバ管理
* SSHセキュリティ監視
* ログ分析
* 脅威検知
* ブルーチーム運用
* サイバーセキュリティラボ構築

---

# Screenshots

## スクリーンショット

### Hydra Attack

### Hydra攻撃画面

(Add screenshot here)

### Splunk Search Results

### Splunk検索結果

(Add screenshot here)

### Dashboard Visualization

### ダッシュボード可視化

(Add screenshot here)

---

# Future Improvements

* Implement Splunk alert automation
* Add fail2ban integration
* Create advanced dashboards
* Add geolocation enrichment
* Integrate Windows Event Logs
* Simulate additional attack techniques

## 今後の改善点

* Splunk アラート自動化
* fail2ban の統合
* 高度なダッシュボード作成
* GeoIP 情報追加
* Windows Event Log 統合
* 追加攻撃手法のシミュレーション

---

# Disclaimer

## 注意事項

This project was created for educational and defensive cybersecurity purposes only. All testing was performed in a controlled lab environment.

本プロジェクトは教育および防御目的のサイバーセキュリティ学習用として作成されています。
すべての検証は管理されたラボ環境内で実施しました。
