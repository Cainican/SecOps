# SSH Brute Force Detection Lab Report

# SSH ブルートフォース攻撃検知ラボ レポート

## Overview

This project demonstrates the detection of SSH brute-force attacks using Splunk Enterprise in a home cybersecurity lab environment.

The objective was to simulate an SSH password attack from Kali Linux against an Ubuntu Server and analyze the resulting authentication logs within Splunk.

## 概要

本プロジェクトでは、ホームサイバーセキュリティラボ環境において、Splunk Enterprise を使用した SSH ブルートフォース攻撃の検知を実施しました。

Kali Linux から Ubuntu Server に対して SSH パスワード攻撃をシミュレーションし、生成された認証ログを Splunk で分析することを目的としています。

## Environment

* Kali Linux (Attacker)
* Ubuntu Server (Target)
* Splunk Enterprise (SIEM)

## 環境

* Kali Linux（攻撃端末）
* Ubuntu Server（対象サーバ）
* Splunk Enterprise（SIEM）

## Network Configuration

* Kali Linux: 192.168.56.101
* Ubuntu Server: 192.168.56.102

## ネットワーク構成

* Kali Linux: 192.168.56.101
* Ubuntu Server: 192.168.56.102

## Attack Simulation

Hydra was used to generate multiple failed SSH login attempts against the Ubuntu Server.

Command used:

```bash
hydra -l root -P testlist.txt -t 4 ssh://192.168.56.102
```

## 攻撃シミュレーション

Hydra を使用し、Ubuntu Server に対して複数回の SSH ログイン失敗試行を発生させました。

使用コマンド:

```bash
hydra -l root -P testlist.txt -t 4 ssh://192.168.56.102
```

## Detection

Authentication events were recorded in:

```text
/var/log/auth.log
```

Splunk successfully ingested the logs and displayed repeated failed login attempts originating from the Kali Linux system.

## 検知

認証イベントは以下のログファイルに記録されました。

```text
/var/log/auth.log
```

Splunk は認証ログの取り込みに成功し、Kali Linux から発生した複数の SSH ログイン失敗イベントを可視化しました。

## Findings

* Multiple failed SSH authentication attempts detected
* Source IP successfully identified
* Splunk successfully indexed Linux authentication logs
* SIEM search queries were created to identify brute-force activity

## 検証結果

* 複数回の SSH 認証失敗を検知
* 攻撃元 IP アドレスを特定
* Linux 認証ログの Splunk へのインデックス化に成功
* ブルートフォース攻撃検知用の SPL クエリを作成

## Skills Demonstrated

* Linux Administration
* SSH Security Monitoring
* Log Analysis
* Splunk Enterprise
* SPL Query Development
* Blue Team Operations

## 習得・実践したスキル

* Linux サーバ管理
* SSH セキュリティ監視
* ログ分析
* Splunk Enterprise 運用
* SPL クエリ作成
* ブルーチーム運用

## Conclusion

The lab successfully simulated and detected SSH brute-force activity within a controlled environment. The project demonstrates foundational SIEM monitoring and threat detection skills applicable to security operations and blue team roles.

## 結論

本ラボでは、管理された環境内で SSH ブルートフォース攻撃のシミュレーションおよび検知に成功しました。

本プロジェクトを通じて、SIEM を活用したログ監視、攻撃検知、分析の基礎スキルを習得し、SOC やブルーチーム業務で活用できる実践的な経験を得ることができました。
