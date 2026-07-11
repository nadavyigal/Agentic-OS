import type { PortfolioData } from "../types";

function clean(value: string | null | undefined) {
  return (value ?? "").replace(/\*\*|`/g, "");
}

export function Overview({ data }: { data: PortfolioData }) {
  const activation = data.numbers.activation.rows.find(
    (row) => row.metric === "Real D7 activation",
  );
  return (
    <div className="section-stack">
      <section className="command-card" aria-labelledby="next-action-title">
        <p className="eyebrow">The one thing to do next</p>
        <h1 id="next-action-title">{clean(data.command.bestNextAction)}</h1>
        <div className="evidence-line">
          <span>From repo evidence</span>
          <time>{data.sources.status}</time>
        </div>
      </section>

      <section aria-labelledby="pulse-title">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Live pulse</p>
            <h2 id="pulse-title">What needs attention</h2>
          </div>
          <span className="section-meta">Founder-safe snapshot</span>
        </div>
        <div className="metric-grid">
          <article className="metric-card">
            <span className="metric-label">Products tracked</span>
            <strong>{data.products.length}</strong>
            <small>Across web, iOS, and the operating system</small>
          </article>
          <article className="metric-card danger">
            <span className="metric-label">Resumely D7</span>
            <strong>{String(activation?.resumely ?? "—")}</strong>
            <small>Real users, founder and QA excluded</small>
          </article>
          <article className="metric-card danger">
            <span className="metric-label">RunSmart D7</span>
            <strong>{String(activation?.runsmart ?? "—")}</strong>
            <small>Real users, founder and QA excluded</small>
          </article>
          <article className="metric-card">
            <span className="metric-label">Tracked agent cost</span>
            <strong>${Math.round(data.usage.totalCostUsd).toLocaleString()}</strong>
            <small>{data.usage.windowDays}-day recorded usage, incomplete coverage</small>
          </article>
        </div>
      </section>

      <section aria-labelledby="priorities-title">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Executive read</p>
            <h2 id="priorities-title">Top priorities</h2>
          </div>
          <span className="section-meta">Reviewed {data.executive.ceoReviewed ?? "unknown"}</span>
        </div>
        <ol className="priority-list">
          {data.executive.top3.map((item, index) => (
            <li key={item.title}>
              <span>{index + 1}</span>
              <div>
                <h3>{clean(item.title)}</h3>
                <p>{clean(item.body)}</p>
              </div>
            </li>
          ))}
        </ol>
      </section>
    </div>
  );
}

export function Products({ data }: { data: PortfolioData }) {
  return (
    <section aria-labelledby="products-title">
      <div className="section-heading page-heading">
        <div>
          <p className="eyebrow">Products</p>
          <h1 id="products-title">Current state from repository evidence</h1>
        </div>
      </div>
      <div className="product-list">
        {data.products.map((product) => (
          <article className="product-card" key={product.name}>
            <header>
              <h2>{product.name}</h2>
              <span className={`status-pill ${product.dirty ? "warning" : "fresh"}`}>
                {product.dirty ? `${product.dirtyCount} unsaved` : product.freshness}
              </span>
            </header>
            <p className="product-state">{clean(product.state)}</p>
            <div className="next-block">
              <span>Do next</span>
              <p>{clean(product.nextAction)}</p>
            </div>
            <footer>Evidence {product.evidenceDate}</footer>
          </article>
        ))}
      </div>
    </section>
  );
}

export function Numbers({ data }: { data: PortfolioData }) {
  return (
    <div className="section-stack">
      <section aria-labelledby="activation-title">
        <div className="section-heading page-heading">
          <div>
            <p className="eyebrow">Numbers</p>
            <h1 id="activation-title">Where real users reach value</h1>
          </div>
        </div>
        <div className="activation-table" role="table" aria-label="Activation comparison">
          <div className="activation-row header" role="row">
            <span role="columnheader">Metric</span>
            <span role="columnheader">Resumely</span>
            <span role="columnheader">RunSmart</span>
          </div>
          {data.numbers.activation.rows.map((row) => (
            <div className="activation-row" role="row" key={String(row.metric)}>
              <strong role="cell">{String(row.metric)}</strong>
              <span role="cell" className={row.bad ? "bad-number" : ""}>{String(row.resumely)}</span>
              <span role="cell" className={row.bad ? "bad-number" : ""}>{String(row.runsmart)}</span>
            </div>
          ))}
        </div>
      </section>

      <section aria-labelledby="funnels-title">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Conversion</p>
            <h2 id="funnels-title">The biggest cliffs</h2>
          </div>
        </div>
        <div className="funnel-grid">
          {data.numbers.funnels.map((funnel) => {
            const max = Math.max(...funnel.steps.map((step) => step[1]), 1);
            return (
              <article className="funnel-card" key={funnel.id}>
                <header>
                  <h3>{funnel.name}</h3>
                  <span>{funnel.tag}</span>
                </header>
                <div className="funnel-steps">
                  {funnel.steps.map(([label, value]) => (
                    <div className="funnel-step" key={label}>
                      <div><span>{label}</span><strong>{value}</strong></div>
                      <div className="bar-track"><i style={{ width: `${Math.max((value / max) * 100, value ? 3 : 0)}%` }} /></div>
                    </div>
                  ))}
                </div>
              </article>
            );
          })}
        </div>
      </section>
    </div>
  );
}

export function Rhythm({ data }: { data: PortfolioData }) {
  return (
    <div className="section-stack">
      <section aria-labelledby="clocks-title">
        <div className="section-heading page-heading">
          <div><p className="eyebrow">Rhythm</p><h1 id="clocks-title">Clocks already running</h1></div>
        </div>
        <div className="clock-list">
          {data.clocks.map((clock, index) => (
            <article key={`${clock.what}-${index}`}>
              <time>{clock.date ?? clock.when ?? "No date"}</time>
              <p>{clock.what}</p>
              <span>{clock.state}</span>
            </article>
          ))}
        </div>
      </section>
      <section aria-labelledby="workflows-title">
        <div className="section-heading"><div><p className="eyebrow">Operating system</p><h2 id="workflows-title">Review cadence</h2></div></div>
        <div className="workflow-list">
          {data.workflows.map((workflow) => (
            <article key={workflow.id}>
              <div><h3>{workflow.name}</h3><p>{workflow.how}</p></div>
              <div className="workflow-date"><span>{workflow.cadence}</span><time>{workflow.lastRan ?? "Never"}</time></div>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}

export function Models({ data }: { data: PortfolioData }) {
  return (
    <div className="section-stack">
      <section aria-labelledby="models-title">
        <div className="section-heading page-heading">
          <div><p className="eyebrow">Models</p><h1 id="models-title">Official facts and our routing policy</h1></div>
          <span className="section-meta">Registry {data.models.asOf ?? "unknown"}</span>
        </div>
        <p className="section-intro">Pricing and model IDs are verified facts. Recommended roles are internal operating preferences.</p>
        <div className="model-table" role="table" aria-label="Model lineup">
          <div className="model-row model-head" role="row"><span>Model</span><span>Vendor</span><span>Input → output</span><span>Our preferred role</span></div>
          {data.models.models.map((model) => (
            <div className="model-row" role="row" key={model.model}>
              <strong>{model.model}</strong><span>{model.vendor}</span><span>${model.in} → ${model.out}</span><p>{model.role}</p>
            </div>
          ))}
        </div>
      </section>
      <section aria-labelledby="coverage-title" className="coverage-card">
        <p className="eyebrow">Cost coverage</p>
        <h2 id="coverage-title">Tracked agent cost, not total AI spend</h2>
        <strong>${data.usage.totalCostUsd.toLocaleString(undefined, { maximumFractionDigits: 0 })}</strong>
        <p>{clean(data.usage.note)}</p>
      </section>
    </div>
  );
}
