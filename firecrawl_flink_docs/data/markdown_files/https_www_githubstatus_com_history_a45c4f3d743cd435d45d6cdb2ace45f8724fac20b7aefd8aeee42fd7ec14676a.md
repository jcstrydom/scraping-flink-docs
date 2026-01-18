![GitHub header](https://user-images.githubusercontent.com/19292210/60553863-044dd200-9cea-11e9-987e-7db84449f215.png)![GitHub header](https://user-images.githubusercontent.com/19292210/60553865-044dd200-9cea-11e9-859c-d6f266e2f01f.png)

#### Incident History

[Previous page](https://www.githubstatus.com/history#back) November 2025 to January 2026 [Next page](https://www.githubstatus.com/history#forward)

#### January 2026

[Disruption with some GitHub services](https://www.githubstatus.com/incidents/zltcsbhqmvqq)

This incident has been resolved. Thank you for your patience and understanding as we addressed this issue. A detailed root cause analysis will be shared as soon as it is available.

Jan 16, 23:53 \- Jan 17, 02:54 UTC

[Incident with Issues and Pull Requests](https://www.githubstatus.com/incidents/q987xpbqjbpl)

On January 15, 2026, between 16:40 UTC and 18:20 UTC, we observed increased latency and timeouts across Issues, Pull Requests, Notifications, Actions, Repositories, API, and Account Login. An average 1.8% of combined web and API requests saw failure, peaking briefly at 10% early on. The majority of impact was observed for unauthenticated users, but authenticated users were impacted as well.

This was caused by an infrastructure update to some of our data stores. Upgrading this infrastructure to a new major version resulted in unexpected resource contention, leading to distributed impact in the form of slow queries and increased timeouts across services that depend on these datasets. We mitigated this by rolling back to the previous stable version.

We are working to improve our validation process for these types of upgrades to catch issues that only occur under high load before full release, improve detection time, and reduce mitigation times in the future.

Jan 15, 16:56 \- 18:54 UTC

[Actions workflow run and job status updates are experiencing delays](https://www.githubstatus.com/incidents/5ccghcfrkv39)

This incident has been resolved. Thank you for your patience and understanding as we addressed this issue. A detailed root cause analysis will be shared as soon as it is available.

Jan 15, 14:24 \- 15:26 UTC

\+ Show All 16 Incidents

#### December 2025

[Incident with Issues and Pull Requests](https://www.githubstatus.com/incidents/ccrzb3ms9j2d)

On December 23, 2025, between 09:15 UTC and 10:32 UTC the Issues and Pull Requests search indexing service was degraded and caused search results to contain stale data up to 3 minutes old for roughly 1.3 million issues and pull requests. This was due to search indexing queues backing up from resource contention caused by a running transition.

We mitigated the incident by cancelling the running transition.

We are working to implement closer monitoring of search infrastructure resource utilization during transitions to reduce our time to detection and mitigation of issues like this one in the future.

Dec 23, 09:56 \- 10:32 UTC

[Disruption with some GitHub services](https://www.githubstatus.com/incidents/y2wxzcfbgbn2)

On December 22, 2025, between 22:01 UTC and 22:32 UTC, unauthenticated requests to github.com were degraded, resulting in slow or timed out page loads and API requests. Unauthenticated requests from Actions jobs, such as release downloads, were also impacted. Authenticated traffic was not impacted. This was due to a severe spike in traffic, primarily to search endpoints.

Our immediate response focused on identifying and mitigating the source of the traffic increase, which along with automated traffic management restored full service for our users.

We improved limiters for load to relevant endpoints and are continuing work to more proactively identify these large changes in traffic volume, improve resilience in critical request flows, and improve our time to mitigation.

Dec 22, 22:31 \- Dec 23, 00:17 UTC

[Disruption with some GitHub services](https://www.githubstatus.com/incidents/49y7x9g06l4x)

On December 18, 2025, between 16:25 UTC and 19:09 UTC the service underlying Copilot policies was degraded and users, organizations, and enterprises were not able to update any policies related to Copilot. No other GitHub services, including other Copilot services were impacted. This was due to a database migration causing a schema drift.

We mitigated the incident by synchronizing the schema. We have hardened the service to make sure schema drift does not cause any further incidents, and will investigate improvements in our deployment pipeline to shorten time to mitigation in the future.

Dec 18, 17:36 \- 19:09 UTC

\+ Show All 15 Incidents

#### November 2025

[Incident with Copilot](https://www.githubstatus.com/incidents/d4775b3j5mwm)

On November 28th, 2025, between approximately 05:51 and 08:04 UTC, Copilot experienced an outage affecting the Claude Sonnet 4.5 model. Users attempting to use this model received an HTTP 400 error, resulting in 4.6% of total chat requests during this timeframe failing. Other models were not impacted.

The issue was caused by a misconfiguration deployed to an internal service which made Claude Sonnet 4.5 unavailable. The problem was identified and mitigated by reverting the change. GitHub is working to improve cross-service deploy safeguards and monitoring to prevent similar incidents in the future.

Nov 28, 06:59 \- 08:23 UTC

[Disruption with some GitHub services](https://www.githubstatus.com/incidents/v6sx0dv6rv2x)

On November 24, 2025, between 12:15 and 15:04 UTC, Codespaces users encountered connection issues when attempting to create a codespace after choosing the recently released VS Code Codespaces extension, version 1.18.1. Users were able to downgrade to the 1.18.0 version of the extension during this period to work around this issue. At peak, the error rate was 19% of connection requests. This was caused by mismatching version dependencies for the released VS Code Codespaces extension.

The connection issues were mitigated by releasing the VS Code Codespaces extension version 1.18.2 that addressed the issue. Users utilizing version 1.18.1 of the VS Code Codespaces extension are advised to upgrade to version >=1.18.2.

We are improving our validation and release process for this extension to ensure functional issues like this are caught before release to customers and to reduce detection and mitigation times for extension issues like this in the future.

Nov 24, 13:10 \- 15:04 UTC

[Disruption with some GitHub services](https://www.githubstatus.com/incidents/zzl9nl31lb35)

Between November 19th, 16:13UTC and November 21st, 12:22UTC, the GitHub Enterprise Importer (GEI) service was in a degraded state, during which time, customers of the service experienced a delay when reclaiming mannequins post-migration.

We have taken steps to prevent similar incidents from occurring in the future.

Nov 19, 16:13 \- Nov 21, 00:22 UTC

\+ Show All 17 Incidents

[← Current Status](https://www.githubstatus.com/) [Powered by Atlassian Statuspage](https://www.atlassian.com/software/statuspage?utm_campaign=www.githubstatus.com&utm_content=SP-notifications&utm_medium=powered-by&utm_source=inapp)

Twitter Widget Iframe

reCAPTCHA

Select all images with **cars** Click verify once there are none left

|     |     |     |
| --- | --- | --- |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA7TjK6uBP6HMNroPngHeMMcv5o5fIq_lO0HC5J8NCxdaV60uTSuJkUS3ZIKoucJ3wOhCeqPaSE3uJguNlCqKQ3XsCm9IwFAa_dKhJ2JpAAnLDG1SN82tBCVdZfZS-wXEiGZdBTiG7czGqdy7yxtTcl8t2tY983cm2BG_MEpiF7gyD26m3qDd8qp1rZB8j7L3eF49bih&k=6LdTS8AUAAAAAOIbCKoCAP4LQku1olYGrywPTaZz) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA7TjK6uBP6HMNroPngHeMMcv5o5fIq_lO0HC5J8NCxdaV60uTSuJkUS3ZIKoucJ3wOhCeqPaSE3uJguNlCqKQ3XsCm9IwFAa_dKhJ2JpAAnLDG1SN82tBCVdZfZS-wXEiGZdBTiG7czGqdy7yxtTcl8t2tY983cm2BG_MEpiF7gyD26m3qDd8qp1rZB8j7L3eF49bih&k=6LdTS8AUAAAAAOIbCKoCAP4LQku1olYGrywPTaZz) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA7TjK6uBP6HMNroPngHeMMcv5o5fIq_lO0HC5J8NCxdaV60uTSuJkUS3ZIKoucJ3wOhCeqPaSE3uJguNlCqKQ3XsCm9IwFAa_dKhJ2JpAAnLDG1SN82tBCVdZfZS-wXEiGZdBTiG7czGqdy7yxtTcl8t2tY983cm2BG_MEpiF7gyD26m3qDd8qp1rZB8j7L3eF49bih&k=6LdTS8AUAAAAAOIbCKoCAP4LQku1olYGrywPTaZz) |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA7TjK6uBP6HMNroPngHeMMcv5o5fIq_lO0HC5J8NCxdaV60uTSuJkUS3ZIKoucJ3wOhCeqPaSE3uJguNlCqKQ3XsCm9IwFAa_dKhJ2JpAAnLDG1SN82tBCVdZfZS-wXEiGZdBTiG7czGqdy7yxtTcl8t2tY983cm2BG_MEpiF7gyD26m3qDd8qp1rZB8j7L3eF49bih&k=6LdTS8AUAAAAAOIbCKoCAP4LQku1olYGrywPTaZz) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA7TjK6uBP6HMNroPngHeMMcv5o5fIq_lO0HC5J8NCxdaV60uTSuJkUS3ZIKoucJ3wOhCeqPaSE3uJguNlCqKQ3XsCm9IwFAa_dKhJ2JpAAnLDG1SN82tBCVdZfZS-wXEiGZdBTiG7czGqdy7yxtTcl8t2tY983cm2BG_MEpiF7gyD26m3qDd8qp1rZB8j7L3eF49bih&k=6LdTS8AUAAAAAOIbCKoCAP4LQku1olYGrywPTaZz) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA7TjK6uBP6HMNroPngHeMMcv5o5fIq_lO0HC5J8NCxdaV60uTSuJkUS3ZIKoucJ3wOhCeqPaSE3uJguNlCqKQ3XsCm9IwFAa_dKhJ2JpAAnLDG1SN82tBCVdZfZS-wXEiGZdBTiG7czGqdy7yxtTcl8t2tY983cm2BG_MEpiF7gyD26m3qDd8qp1rZB8j7L3eF49bih&k=6LdTS8AUAAAAAOIbCKoCAP4LQku1olYGrywPTaZz) |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA7TjK6uBP6HMNroPngHeMMcv5o5fIq_lO0HC5J8NCxdaV60uTSuJkUS3ZIKoucJ3wOhCeqPaSE3uJguNlCqKQ3XsCm9IwFAa_dKhJ2JpAAnLDG1SN82tBCVdZfZS-wXEiGZdBTiG7czGqdy7yxtTcl8t2tY983cm2BG_MEpiF7gyD26m3qDd8qp1rZB8j7L3eF49bih&k=6LdTS8AUAAAAAOIbCKoCAP4LQku1olYGrywPTaZz) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA7TjK6uBP6HMNroPngHeMMcv5o5fIq_lO0HC5J8NCxdaV60uTSuJkUS3ZIKoucJ3wOhCeqPaSE3uJguNlCqKQ3XsCm9IwFAa_dKhJ2JpAAnLDG1SN82tBCVdZfZS-wXEiGZdBTiG7czGqdy7yxtTcl8t2tY983cm2BG_MEpiF7gyD26m3qDd8qp1rZB8j7L3eF49bih&k=6LdTS8AUAAAAAOIbCKoCAP4LQku1olYGrywPTaZz) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA7TjK6uBP6HMNroPngHeMMcv5o5fIq_lO0HC5J8NCxdaV60uTSuJkUS3ZIKoucJ3wOhCeqPaSE3uJguNlCqKQ3XsCm9IwFAa_dKhJ2JpAAnLDG1SN82tBCVdZfZS-wXEiGZdBTiG7czGqdy7yxtTcl8t2tY983cm2BG_MEpiF7gyD26m3qDd8qp1rZB8j7L3eF49bih&k=6LdTS8AUAAAAAOIbCKoCAP4LQku1olYGrywPTaZz) |

Please try again.

Please select all matching images.

Please also check the new images.

Please select around the object, or reload if there are none.

Verify

reCAPTCHA

Select all squares with **bicycles** If there are none, click skip

|     |     |     |     |
| --- | --- | --- | --- |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA75Kt-UxYA3ovDQxosUYsOveAPoZ0t_oWNie8NogR6y0dRA8ckzfUmC30OriuOBs1pgwjMciNaad3LuQfXEHppgYMQy5gzJqUsmm1mQyKKd7rIuPKa4u8ZLXhqH3E_gWuemZUpZdHh6wUOzUTIf38b0J0Y6X5hlkypckCzkXJ4Q4wDCkxVHWkBt_UUOItRKKz_y3C2m&k=6LcQ-b0UAAAAAJjfdwO_-ozGC-CzWDj4Pm1kJ2Ah) |

Please try again.

Please select all matching images.

Please also check the new images.

Please select around the object, or reload if there are none.

Skip

reCAPTCHA

Select all images with **crosswalks** Click verify once there are none left.

|     |     |     |
| --- | --- | --- |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA4rO2VGdOdhIkCtHMDq1Xdb7bvzJL6cHU68QACxFP-LenlhxS4H2SPmgVbHHL2_QxcV_KsORA2jW_-EZ84wNUcwhgDm-fx3ummQ7RvkikyNdm39rd_mzM_SbhQRoKZypc6y4oomDgDbpPyEPNLlK80ywllxFOgM5XfbNAl6QB0N12NL2jT6yXsAH5iQVcu9eCo6BNRN&k=6LcH-b0UAAAAACVQtMb14LBhflMA9y0Nmu7l_W6d) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA4rO2VGdOdhIkCtHMDq1Xdb7bvzJL6cHU68QACxFP-LenlhxS4H2SPmgVbHHL2_QxcV_KsORA2jW_-EZ84wNUcwhgDm-fx3ummQ7RvkikyNdm39rd_mzM_SbhQRoKZypc6y4oomDgDbpPyEPNLlK80ywllxFOgM5XfbNAl6QB0N12NL2jT6yXsAH5iQVcu9eCo6BNRN&k=6LcH-b0UAAAAACVQtMb14LBhflMA9y0Nmu7l_W6d) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA4rO2VGdOdhIkCtHMDq1Xdb7bvzJL6cHU68QACxFP-LenlhxS4H2SPmgVbHHL2_QxcV_KsORA2jW_-EZ84wNUcwhgDm-fx3ummQ7RvkikyNdm39rd_mzM_SbhQRoKZypc6y4oomDgDbpPyEPNLlK80ywllxFOgM5XfbNAl6QB0N12NL2jT6yXsAH5iQVcu9eCo6BNRN&k=6LcH-b0UAAAAACVQtMb14LBhflMA9y0Nmu7l_W6d) |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA4rO2VGdOdhIkCtHMDq1Xdb7bvzJL6cHU68QACxFP-LenlhxS4H2SPmgVbHHL2_QxcV_KsORA2jW_-EZ84wNUcwhgDm-fx3ummQ7RvkikyNdm39rd_mzM_SbhQRoKZypc6y4oomDgDbpPyEPNLlK80ywllxFOgM5XfbNAl6QB0N12NL2jT6yXsAH5iQVcu9eCo6BNRN&k=6LcH-b0UAAAAACVQtMb14LBhflMA9y0Nmu7l_W6d) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA4rO2VGdOdhIkCtHMDq1Xdb7bvzJL6cHU68QACxFP-LenlhxS4H2SPmgVbHHL2_QxcV_KsORA2jW_-EZ84wNUcwhgDm-fx3ummQ7RvkikyNdm39rd_mzM_SbhQRoKZypc6y4oomDgDbpPyEPNLlK80ywllxFOgM5XfbNAl6QB0N12NL2jT6yXsAH5iQVcu9eCo6BNRN&k=6LcH-b0UAAAAACVQtMb14LBhflMA9y0Nmu7l_W6d) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA4rO2VGdOdhIkCtHMDq1Xdb7bvzJL6cHU68QACxFP-LenlhxS4H2SPmgVbHHL2_QxcV_KsORA2jW_-EZ84wNUcwhgDm-fx3ummQ7RvkikyNdm39rd_mzM_SbhQRoKZypc6y4oomDgDbpPyEPNLlK80ywllxFOgM5XfbNAl6QB0N12NL2jT6yXsAH5iQVcu9eCo6BNRN&k=6LcH-b0UAAAAACVQtMb14LBhflMA9y0Nmu7l_W6d) |
| ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA4rO2VGdOdhIkCtHMDq1Xdb7bvzJL6cHU68QACxFP-LenlhxS4H2SPmgVbHHL2_QxcV_KsORA2jW_-EZ84wNUcwhgDm-fx3ummQ7RvkikyNdm39rd_mzM_SbhQRoKZypc6y4oomDgDbpPyEPNLlK80ywllxFOgM5XfbNAl6QB0N12NL2jT6yXsAH5iQVcu9eCo6BNRN&k=6LcH-b0UAAAAACVQtMb14LBhflMA9y0Nmu7l_W6d) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA4rO2VGdOdhIkCtHMDq1Xdb7bvzJL6cHU68QACxFP-LenlhxS4H2SPmgVbHHL2_QxcV_KsORA2jW_-EZ84wNUcwhgDm-fx3ummQ7RvkikyNdm39rd_mzM_SbhQRoKZypc6y4oomDgDbpPyEPNLlK80ywllxFOgM5XfbNAl6QB0N12NL2jT6yXsAH5iQVcu9eCo6BNRN&k=6LcH-b0UAAAAACVQtMb14LBhflMA9y0Nmu7l_W6d) | ![](https://www.recaptcha.net/recaptcha/enterprise/payload?p=06AFcWeA4rO2VGdOdhIkCtHMDq1Xdb7bvzJL6cHU68QACxFP-LenlhxS4H2SPmgVbHHL2_QxcV_KsORA2jW_-EZ84wNUcwhgDm-fx3ummQ7RvkikyNdm39rd_mzM_SbhQRoKZypc6y4oomDgDbpPyEPNLlK80ywllxFOgM5XfbNAl6QB0N12NL2jT6yXsAH5iQVcu9eCo6BNRN&k=6LcH-b0UAAAAACVQtMb14LBhflMA9y0Nmu7l_W6d) |

Please try again.

Please select all matching images.

Please also check the new images.

Please select around the object, or reload if there are none.

Verify