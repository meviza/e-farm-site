import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

// Brand green renders well on both light and dark backgrounds.
const BRAND = "#1f7a44";

// Anchors: 2025 = 17.73B, 2030 = 56.26B (MarketsandMarkets, 2025).
// Interpolate every year at the implied 26% CAGR for intermediate points.
const ANCHOR_2025 = 17.73;
const CAGR = 0.26;
const data = Array.from({ length: 8 }, (_, i) => {
  const year = 2023 + i;
  const t = year - 2025;
  const value = ANCHOR_2025 * Math.pow(1 + CAGR, t);
  return { year: String(year), value: Number(value.toFixed(2)) };
});

type StatProps = { labels: Record<string, string> };

export default function MarketChart({ labels }: StatProps) {
  const stats = [
    { value: labels.cagrValue, label: labels.cagrLabel },
    { value: labels.sizeValue, label: labels.sizeLabel },
    { value: labels.laborValue, label: labels.laborLabel },
    { value: labels.ghValue, label: labels.ghLabel },
  ];

  return (
    <div className="grid gap-8 lg:grid-cols-[1.6fr_1fr]">
      <figure className="rounded-2xl border border-border bg-surface p-5 shadow-[var(--shadow)]">
        <figcaption className="mb-4 text-sm font-semibold text-text">
          {labels.chartTitle}
        </figcaption>
        <div className="h-72 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={data} margin={{ top: 8, right: 8, left: -8, bottom: 0 }}>
              <defs>
                <linearGradient id="mktFill" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stopColor={BRAND} stopOpacity={0.35} />
                  <stop offset="100%" stopColor={BRAND} stopOpacity={0.02} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} />
              <XAxis
                dataKey="year"
                tick={{ fill: "var(--text-muted)", fontSize: 12 }}
                tickLine={false}
                axisLine={{ stroke: "var(--border)" }}
              />
              <YAxis
                tick={{ fill: "var(--text-muted)", fontSize: 12 }}
                tickLine={false}
                axisLine={false}
                width={44}
                tickFormatter={(v) => `$${v}B`}
              />
              <Tooltip
                contentStyle={{
                  background: "var(--surface)",
                  border: "1px solid var(--border)",
                  borderRadius: 12,
                  color: "var(--text)",
                  fontSize: 13,
                }}
                labelStyle={{ color: "var(--text-muted)" }}
                formatter={(v: number) => [`$${v}B`, "Market size"]}
              />
              <Area
                type="monotone"
                dataKey="value"
                stroke={BRAND}
                strokeWidth={2.5}
                fill="url(#mktFill)"
                dot={{ r: 2.5, fill: BRAND }}
                activeDot={{ r: 5 }}
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
        <p className="mt-3 font-mono text-xs text-muted">{labels.chartSource}</p>
      </figure>

      <div className="grid grid-cols-2 gap-4 lg:grid-cols-1">
        {stats.map((s) => (
          <div
            key={s.label}
            className="rounded-2xl border border-border bg-surface p-5 shadow-[var(--shadow)]"
          >
            <div className="text-3xl font-bold tracking-tight text-brand">{s.value}</div>
            <div className="mt-1 text-sm text-muted">{s.label}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
