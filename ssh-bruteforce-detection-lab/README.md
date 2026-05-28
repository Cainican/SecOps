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
