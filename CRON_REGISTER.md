# CRON_REGISTER.md - System Timetable & Task Registry

ဤဖိုင်သည် Cosmos Team ၏ စနစ်တစ်ခုလုံးတွင် Run နေသော အချိန်ကိုက်လုပ်ဆောင်ချက် (Cron Jobs) များအားလုံးကို စုစည်းမှတ်တမ်းတင်ထားသော Registry ဖြစ်သည်။ အေးဂျင့်အားလုံး အလုပ်အသစ်တစ်ခု မစမီ ဤနေရာတွင် အချိန်တိုက်ဆိုင်မှု ရှိ၊ မရှိ မဖြစ်မနေ စစ်ဆေးရမည်။

## 🔴 CRITICAL DIRECTIVE (MANDATORY)
၁။ **Check Before You Act:** အေးဂျင့်တိုင်းသည် Cron Job သို့မဟုတ် Schedule တစ်ခုခု မသတ်မှတ်မီ ဤဖိုင်ကို အရင်ဖတ်ပါ။ လက်ရှိ Run နေသော အလုပ်များနှင့် အချိန်တိုက်နေပါက ထပ်မံ မထည့်ပါနှင့်။
၂။ **Must Register:** မည်သည့် အချိန်ကိုက်အလုပ်ကိုမဆို ဤဖိုင်တွင် လာရောက် စာရင်းသွင်းရမည်။ စာရင်းမသွင်းဘဲ Run နေသော အလုပ်များကို တွေ့ရှိပါက David သို့မဟုတ် Ko Sai မှ ချက်ချင်း ရပ်နား (Kill/Stop) ပိုင်ခွင့်ရှိသည်။
၃။ **Conflict Resolution:** အချိန်တိုက်ဆိုင်နေပါက Priority မြင့်သော အလုပ်ကို ဦးစားပေးပါ။

---

## 🟢 SECTION 1: ACTIVE JOBS (လက်ရှိ Run နေသော အလုပ်များ)

| ID | Schedule | Task Description | Owner | Priority | Level | Status |
|:---|:---|:---|:---|:---|:---|:---|
| `sys-sync` | `0 */6 * * *` | GitHub Sync & Backup | System | High | System | Active |
| `sys-brain` | `0 0,6,12,18 * * *` | Process Second Brain Data | System | High | System | Active |
| `sys-watch` | `*/5 * * * *` | Resource Watchdog (RAM/CPU) | Ko Sai | High | System | Active |
| `oc-dist-1` | `0 3 * * *` | Daily Memory Distillation | David | High | OpenClaw | Active |
| `oc-lib-da` | `0 0,12 * * *` | David Librarian (Memory Sync) | David | High | OpenClaw | Active |
| `oc-lib-ks` | `15 0,12 * * *` | Ko Sai Librarian (Tech Sync) | Ko Sai | High | OpenClaw | Active |
| `oc-log-clean`| `0 2 * * 0` | Weekly Log Cleanup & Distillation | Ko Sai | High | OpenClaw | Active |
| `sys-cal` | `0 21 * * *` | Google Calendar Ivy Lee Planning | Nolan | Medium | System | Active |
| `sys-gbn` | `0 4 * * *` | GBN Engine Processing | System | Medium | System | Active |
| `sys-met` | `30 23 * * *` | Metrics Collection | System | Medium | System | Active |

---

## 🟡 SECTION 2: PLANNED JOBS (လုပ်ဆောင်ရန် စီစဉ်ထားသည်များ)

| ID | Schedule | Task Description | Owner | Priority | Level | Status |
|:---|:---|:---|:---|:---|:---|:---|
| `plan-ram` | `*/15 * * * *` | Check RAM/CPU and alert Nolan | Ko Sai | High | OpenClaw | Planned |
| `plan-health`| `0 * * * *` | OpenClaw Service Health Check | Ko Sai | High | OpenClaw | Planned |
| `plan-brief` | `0 8 * * *` | Morning Briefing (Daily) | Ko Sai | High | OpenClaw | Planned |
| `plan-audit` | `0 */6 * * *` | Health Audit & Backup Integrity | Ko Sai | High | OpenClaw | Planned |

---
*Last Updated: 2026-03-02 by David (Manager)*
