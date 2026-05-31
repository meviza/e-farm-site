import { useMemo, useState } from "react";
import { ArrowDown, ArrowUp, ChevronsUpDown } from "lucide-react";
import { competitors, type Competitor } from "../../data/competitors";

type SortKey = keyof Omit<Competitor, "isUs">;
type Dir = "asc" | "desc";

const columns: { key: SortKey; label: string }[] = [
  { key: "company", label: "Company" },
  { key: "country", label: "Country" },
  { key: "crops", label: "Crops" },
  { key: "tech", label: "Core tech" },
  { key: "performance", label: "Reported performance" },
  { key: "funding", label: "Funding" },
  { key: "stage", label: "Stage" },
];

type Props = { usLabel?: string };

export default function CompetitorMatrix({ usLabel = "That’s us" }: Props) {
  const [sortKey, setSortKey] = useState<SortKey>("company");
  const [dir, setDir] = useState<Dir>("asc");

  const sorted = useMemo(() => {
    const rows = [...competitors];
    rows.sort((a, b) => {
      const cmp = a[sortKey].localeCompare(b[sortKey], undefined, { numeric: true });
      return dir === "asc" ? cmp : -cmp;
    });
    return rows;
  }, [sortKey, dir]);

  function onSort(key: SortKey) {
    if (key === sortKey) {
      setDir((d) => (d === "asc" ? "desc" : "asc"));
    } else {
      setSortKey(key);
      setDir("asc");
    }
  }

  return (
    <div className="overflow-x-auto rounded-2xl border border-border bg-surface shadow-[var(--shadow)]">
      <table className="w-full min-w-[860px] border-collapse text-left text-sm">
        <thead>
          <tr className="border-b border-border bg-surface-2">
            {columns.map((col) => {
              const active = col.key === sortKey;
              return (
                <th
                  key={col.key}
                  scope="col"
                  aria-sort={active ? (dir === "asc" ? "ascending" : "descending") : "none"}
                  className="p-0"
                >
                  <button
                    type="button"
                    onClick={() => onSort(col.key)}
                    className="flex w-full items-center gap-1.5 px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide text-muted transition-colors hover:text-text focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand"
                  >
                    <span>{col.label}</span>
                    {active ? (
                      dir === "asc" ? (
                        <ArrowUp className="h-3.5 w-3.5 text-brand" aria-hidden="true" />
                      ) : (
                        <ArrowDown className="h-3.5 w-3.5 text-brand" aria-hidden="true" />
                      )
                    ) : (
                      <ChevronsUpDown className="h-3.5 w-3.5 opacity-40" aria-hidden="true" />
                    )}
                  </button>
                </th>
              );
            })}
          </tr>
        </thead>
        <tbody>
          {sorted.map((row) => (
            <tr
              key={row.company}
              className={
                row.isUs
                  ? "border-b border-border bg-brand-soft"
                  : "border-b border-border hover:bg-surface-2"
              }
            >
              <th scope="row" className="px-4 py-3 align-top font-semibold text-text">
                <span className="flex flex-col gap-1">
                  <span className={row.isUs ? "text-brand" : undefined}>{row.company}</span>
                  {row.isUs && (
                    <span className="inline-flex w-fit rounded-full bg-brand px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wide text-white">
                      {usLabel}
                    </span>
                  )}
                </span>
              </th>
              <td className="px-4 py-3 align-top text-muted">{row.country}</td>
              <td className="px-4 py-3 align-top text-muted">{row.crops}</td>
              <td className="px-4 py-3 align-top text-muted">{row.tech}</td>
              <td className="px-4 py-3 align-top text-muted">{row.performance}</td>
              <td className="px-4 py-3 align-top text-muted">{row.funding}</td>
              <td className="px-4 py-3 align-top text-muted">{row.stage}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
