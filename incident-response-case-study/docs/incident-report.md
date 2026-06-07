# Incident Report / インシデント報告書

## Incident Summary / インシデント概要

A brute-force SSH attack was launched from a Kali Linux VM against an Ubuntu Server VM hosting an SSH service and Splunk Enterprise Free.

Kali Linux VMから、SSHサービスおよびSplunk Enterprise Freeを実行するUbuntu Server VMに対してSSHブルートフォース攻撃が実行された。

---

## Detection / 検知

Splunk detected multiple failed SSH authentication attempts originating from a single source IP address.

Splunkにより、単一の送信元IPアドレスから多数のSSH認証失敗イベントが検知された。

The activity was identified through authentication log monitoring and event analysis.

この活動は認証ログの監視およびイベント分析によって特定された。

---

## Investigation / 調査

Analysis of authentication logs revealed:

* Multiple failed login attempts
* Repeated authentication failures from the same source IP address
* A successful SSH login following numerous failed attempts

認証ログの分析により、以下のことが判明した。

* 複数回のログイン失敗
* 同一送信元IPアドレスからの繰り返しの認証失敗
* 多数の失敗後に発生したSSHログイン成功

The source IP responsible for the failed login attempts was also associated with the successful authentication event.

認証失敗イベントを発生させた送信元IPアドレスは、認証成功イベントにも関連していた。

---

## Findings / 調査結果

The investigation confirmed that the attacker successfully authenticated to the Ubuntu Server using valid credentials.

調査の結果、攻撃者は有効な認証情報を使用してUbuntu Serverへの認証に成功したことが確認された。

The sequence of events indicates a successful brute-force compromise of the SSH service.

一連のイベントは、SSHサービスに対するブルートフォース攻撃が成功したことを示している。

---

## Impact Assessment / 影響評価

Successful authentication provided the attacker with access to the target system.

認証成功により、攻撃者はターゲットシステムへアクセス可能となった。

No destructive or malicious post-authentication activity was performed as this incident occurred within a controlled laboratory environment.

本インシデントは管理された検証環境内で実施されたため、認証後の破壊的または悪意のある活動は行われなかった。

---

## Root Cause / 根本原因

The use of weak credentials allowed the brute-force attack to successfully compromise the target system.

脆弱な認証情報の使用により、ブルートフォース攻撃によるシステム侵害が可能となった。

---

## Recommendations / 推奨事項

* Enforce strong password policies

* Use SSH key-based authentication

* Deploy Fail2Ban to block repeated failed login attempts

* Implement account lockout policies

* Continue monitoring authentication logs with Splunk

* 強力なパスワードポリシーを適用する

* SSH鍵認証を使用する

* Fail2Banを導入し認証失敗を制限する

* アカウントロックアウトポリシーを設定する

* Splunkによる認証ログ監視を継続する

---

## Conclusion / 結論

The attack was successfully detected, investigated, and documented using Splunk Enterprise.

本攻撃はSplunk Enterpriseを用いて検知・調査・文書化することができた。

This project demonstrates fundamental incident response and security monitoring techniques within a home lab environment.

本プロジェクトは、ホームラボ環境における基本的なインシデントレスポンスおよびセキュリティ監視技術を実証するものである。
