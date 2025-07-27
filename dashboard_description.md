### Dashboard: Moderation Pipeline Metrics

The **Moderation Pipeline Metrics Dashboard** provides comprehensive visibility into the performance, throughput, and efficiency of the entire content moderation workflow. Built using **Amazon QuickSight**, the dashboard ingests real-time metrics from Redshift and Lambda logs, giving stakeholders actionable insights into model routing decisions, moderator loads, latency, and content disposition outcomes. This dashboard was designed to be scalable and modular, supporting experimentation and operations monitoring at scale.

---

#### 1. **Executive Summary Panel**

* **Overview Tiles:**

  * Total content pieces routed (Today / Week / Month)
  * Average moderation cost per item
  * Total flagged vs. resolved items
  * Overall accuracy of ML routing models
* **KPI Scorecards:**

  * Average moderation time per item
  * Success rate of auto-resolved content by ML models
  * Percentage of re-routed content due to uncertainty thresholds

This panel helps product managers and executive stakeholders monitor health and effectiveness of the moderation ecosystem.

---

#### 2. **Routing Efficiency Visualization**

* **Sankey Diagram:**

  * Tracks flow of content from ingestion → ML scoring → final human moderator assignment
  * Visualizes routing splits by model confidence and type (text/image/video)
* **Routing Success Funnel:**

  * Number of items that passed each stage without human intervention
  * Drop-offs at each moderation logic branch

These charts are essential for data engineers and ML teams to understand if content is being distributed effectively across the pipeline.

---

#### 3. **Moderator Load Heatmap**

* **Moderator Activity Table:**

  * Moderator ID, number of reviews completed, SLA breaches, escalations
* **Geographic Distribution Map:**

  * Shows average workload across moderation centers worldwide
* **Daily Load Trends:**

  * Time series plots of incoming content volumes and moderator backlog over time

This section helps workforce management teams balance reviewer assignments and shift planning.

---

#### 4. **Latency & Cost Metrics**

* **End-to-End Pipeline Latency (ms):**

  * Breakdown by processing step (ingestion, ML classification, routing, human moderation)
* **Cost-to-Serve Charts:**

  * Real-time cost model showing per-item moderation cost by type (ML only, human-assisted, escalated)
  * Forecast of moderation spend by content type

Enables strategic decision making to identify cost bottlenecks and optimize for high-throughput moderation.

---

#### 5. **Error Analysis & Quality Metrics**

* **Flag vs. Resolution Accuracy:**

  * Heatmap showing false positives/negatives by content category
* **Escalation Root Cause Tree:**

  * Tracks why content was escalated beyond auto-moderation: model drift, lack of coverage, or complexity
* **Audit Trail Explorer:**

  * Searchable drill-down of specific content items with model prediction, reviewer decision, and latency breakdown

This panel supports continuous model retraining, feedback loops, and compliance audits.

---

#### 6. **Alerts & Anomaly Detection Panel**

* **Auto-generated alerts:**

  * Triggered when moderator backlog exceeds threshold
  * Latency spikes or data ingestion failures
  * Sudden shifts in flagged content ratio by geography or type
* **Anomaly Time Series:**

  * Uses z-score and rolling averages to surface outlier behavior in moderation volumes

These alerts feed into operational runbooks and Slack alerts to allow real-time triage.

---

#### 7. **Dashboard Maintenance & Governance**

* **Data Refresh:**

  * Real-time streaming via Lambda + Kinesis → Redshift
  * Batch mode fallback with 15-minute latency from S3
* **Access Controls:**

  * Row-level security enforced for regional moderators
  * Admin and audit roles for compliance users
* **Documentation & Definitions:**

  * Built-in tooltips and metrics dictionary to explain KPIs and pipeline logic

---

### Value Delivered

* Reduced average moderation latency by 25% through visibility into routing gaps
* Improved ML model precision by 18% via continuous feedback loop powered by audit dashboard
* Enhanced stakeholder trust and transparency via real-time SLA tracking

This dashboard has become a core operational asset, used daily by engineering, policy, and support teams to maintain platform integrity and optimize resources.
