# SSH Brute-Force Incident Response Case Study / SSHブルートフォース攻撃 インシデントレスポンス事例

## Overview / 概要

This project simulates an SSH brute-force attack against an Ubuntu Server and demonstrates how the attack can be detected, investigated, and documented using Splunk Enterprise.

本プロジェクトでは、Ubuntu Serverに対するSSHブルートフォース攻撃をシミュレーションし、Splunk Enterpriseを使用して攻撃の検知・調査・文書化を行った。

---

## Project Structure / プロジェクト構成

```text
incident-response-case-study/
│
├── README.md
├── attack-scripts/
│   └── hydra-command.txt
├── searches/
│   └── splunk-searches.txt
├── docs/
│   └── incident-report.md
├── screenshots/
│   ├── 01-hydra-bruteforce-command.jpg
│   ├── 02-failed-password-attempts.jpg
│   ├── 03-successful-login-event.jpg
│   ├── 04-source-ip-investigation.jpg
│   ├── 05-timeline-analysis.jpg
│   ├── 06-incident-summary.jpg
│   └── 07-splunk-dashboard.jpg
```
---

## Objective / 目的

The objective of this project is to gain hands-on experience with:

* Attack simulation
* Log collection and monitoring
* Security event detection
* Incident investigation
* Incident response documentation

本プロジェクトの目的は、以下の実践的なスキルを習得することである。

* 攻撃シミュレーション
* ログ収集と監視
* セキュリティイベント検知
* インシデント調査
* インシデントレスポンス文書作成

---

## Lab Architecture / ラボのアーキテクチャ

```text
Windows 11 Host / Windows 11 ホスト
│
├── Kali Linux VM / Kali Linux 仮想マシン
│   └── Attacker Machine / 攻撃用マシン
│
└── Ubuntu Server VM / Ubuntu Server 仮想マシン
    ├── SSH Target Server / SSHターゲットサーバー
    └── Splunk Enterprise Free / Splunk Enterprise Free（ログ分析・SIEM）
```

---

## Tools Used / 使用ツール

| Tool                   | Purpose                     |
| ---------------------- | --------------------------- |
| Windows 11             | Host Operating System       |
| Kali Linux             | Attack Platform             |
| Ubuntu Server          | Target System               |
| Hydra                  | SSH Brute-Force Tool        |
| OpenSSH                | SSH Service                 |
| Splunk Enterprise Free | Log Collection and Analysis |

| ツール                    | 用途             |
| ---------------------- | -------------- |
| Windows 11             | ホストOS          |
| Kali Linux             | 攻撃環境           |
| Ubuntu Server          | ターゲット環境        |
| Hydra                  | SSHブルートフォースツール |
| OpenSSH                | SSHサービス        |
| Splunk Enterprise Free | ログ収集・分析        |

---

## Attack Scenario / 攻撃シナリオ

A brute-force attack was launched from the Kali Linux virtual machine against the SSH service running on the Ubuntu Server.

Hydra was used to repeatedly attempt password authentication until valid credentials were discovered.

Kali Linux仮想マシンからUbuntu Server上で動作するSSHサービスに対してブルートフォース攻撃を実施した。

Hydraを使用して複数回の認証試行を行い、有効な認証情報の特定を試みた。

---

## Investigation Process / 調査手順

### Step 1 – Attack Execution / 攻撃実行

Hydra was used to generate multiple SSH authentication attempts against the target system.

Hydraを使用してターゲットシステムへ複数回のSSH認証試行を実施した。

---

### Step 2 – Detection / 検知

Splunk was used to monitor authentication logs and identify failed login attempts.

Splunkを使用して認証ログを監視し、ログイン失敗イベントを検知した。

---

### Step 3 – Investigation / 調査

Authentication events were analyzed to identify:

* Repeated failed logins
* Source IP address
* Successful login events
* Event timeline

認証イベントを分析し、以下を確認した。

* 繰り返し発生したログイン失敗
* 送信元IPアドレス
* ログイン成功イベント
* イベント発生時系列

---

### Step 4 – Correlation / 相関分析

Failed authentication events and successful authentication events were correlated using the source IP address.

送信元IPアドレスを利用して、認証失敗イベントと認証成功イベントの関連付けを実施した。

---

### Step 5 – Findings and Recommendations / 結果と対策

The attack activity was confirmed and mitigation recommendations were documented.

攻撃活動を確認し、再発防止のための対策を整理した。

---

## Splunk Searches Used / 使用したSplunk検索

### Failed Authentication Attempts

```spl
index=* "Failed password"
```

### Successful Authentication Events

```spl
index=* "Accepted password"
```

### Authentication Timeline

```spl
index=* ("Failed password" OR "Accepted password")
```

### Source IP Investigation

```spl
index=* "192.168.56.101"
```

---

## Findings / 調査結果

### Initial Detection / 初期検知

Splunk detected a large number of failed SSH authentication attempts originating from a single IP address.

Splunkにより、単一のIPアドレスから大量のSSH認証失敗試行が検知された。

### Investigation / 調査

Further analysis revealed:

* Repeated failed login attempts
* Same source IP across events
* Successful login after multiple failures

詳細な分析の結果、以下が判明した。

* 繰り返しのログイン失敗試行
* すべてのイベントで同一の送信元IPアドレスを確認
* 複数回の失敗後にログイン成功を確認

### Impact / 影響

The attacker successfully authenticated to the Ubuntu Server using valid credentials.

攻撃者は有効な認証情報を使用してUbuntu Serverへの認証に成功した。

### Root Cause / 根本原因

The use of weak credentials allowed the brute-force attack to successfully compromise the target system.

脆弱な認証情報の使用により、ブルートフォース攻撃によるシステム侵害が可能となった。

---

## Recommendations / 推奨事項

* Disable password authentication

* Use SSH key authentication

* Implement Fail2Ban

* Enforce strong passwords

* Monitor authentication logs continuously

* Configure account lockout policies

* パスワード認証を無効化する

* SSH鍵認証を使用する

* Fail2Banを導入する

* 強力なパスワードを適用する

* 認証ログを継続的に監視する

* アカウントロックアウトポリシーを設定する

---

## Skills Demonstrated / 習得スキル

- Linux Administration
- SSH Security Monitoring
- Splunk SIEM
- Log Analysis
- Event Correlation
- Incident Response
- Security Investigation
- Brute-Force Attack Detection

- Linux管理
- SSHセキュリティ監視
- Splunk SIEM
- ログ分析
- イベント相関分析
- インシデントレスポンス
- セキュリティ調査
- ブルートフォース攻撃検知

---

## Lessons Learned / 学習内容

Through this project, I gained practical experience with:

* Linux authentication logs
* SSH brute-force attack detection
* Splunk log analysis
* Event correlation
* Incident investigation methodology
* Security monitoring fundamentals

本プロジェクトを通じて以下の実践的なスキルを習得した。

* Linux認証ログ分析
* SSHブルートフォース攻撃の検知
* Splunkログ分析
* イベント相関分析
* インシデント調査手法
* セキュリティ監視の基礎

---

## Author / 作成者

Casper Eliassen

Student, HAL Tokyo / 学生、HAL東京
Advanced Information Processing Course (高度情報処理学科)

Expected Graduation: March 2028
