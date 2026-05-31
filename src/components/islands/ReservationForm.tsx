import { useState, type FormEvent } from "react";

type Labels = {
  company: string;
  contact: string;
  email: string;
  country: string;
  crop: string;
  cropSelect: string;
  cropStrawberry: string;
  cropTomato: string;
  cropPepper: string;
  cropCucumber: string;
  cropEggplant: string;
  cropOther: string;
  size: string;
  message: string;
  messagePlaceholder: string;
  required: string;
  submit: string;
  sending: string;
  success: string;
  error: string;
  subject: string;
};

type Props = { endpoint: string; labels: Labels };

type Status = "idle" | "sending" | "success" | "error";

export default function ReservationForm({ endpoint, labels: l }: Props) {
  const [status, setStatus] = useState<Status>("idle");

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const form = e.currentTarget;
    setStatus("sending");
    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { Accept: "application/json" },
        body: new FormData(form),
      });
      if (res.ok) {
        setStatus("success");
        form.reset();
      } else {
        setStatus("error");
      }
    } catch {
      setStatus("error");
    }
  }

  const crops = [
    l.cropStrawberry,
    l.cropTomato,
    l.cropPepper,
    l.cropCucumber,
    l.cropEggplant,
    l.cropOther,
  ];

  const fieldClass =
    "w-full rounded-lg border border-border bg-bg px-3 py-2.5 text-sm text-text placeholder:text-muted focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand";
  const labelClass = "mb-1.5 block text-sm font-medium text-text";

  if (status === "success") {
    return (
      <div
        role="status"
        className="rounded-2xl border border-brand bg-brand-soft p-6 text-sm font-medium text-brand-strong shadow-[var(--shadow)]"
      >
        {l.success}
      </div>
    );
  }

  return (
    <form
      onSubmit={onSubmit}
      className="rounded-2xl border border-border bg-surface p-6 shadow-[var(--shadow)] sm:p-8"
      noValidate
    >
      {/* Honeypot — hidden from humans, catches bots */}
      <input
        type="text"
        name="_gotcha"
        tabIndex={-1}
        autoComplete="off"
        style={{ display: "none" }}
        aria-hidden="true"
      />
      <input type="hidden" name="_subject" value={l.subject} />

      <div className="grid gap-4 sm:grid-cols-2">
        <div>
          <label className={labelClass} htmlFor="company">
            {l.company}
          </label>
          <input id="company" name="company" type="text" className={fieldClass} />
        </div>
        <div>
          <label className={labelClass} htmlFor="contact">
            {l.contact} <span className="text-accent">*</span>
          </label>
          <input id="contact" name="contact" type="text" required className={fieldClass} />
        </div>
        <div>
          <label className={labelClass} htmlFor="email">
            {l.email} <span className="text-accent">*</span>
          </label>
          <input id="email" name="email" type="email" required className={fieldClass} />
        </div>
        <div>
          <label className={labelClass} htmlFor="country">
            {l.country}
          </label>
          <input id="country" name="country" type="text" className={fieldClass} />
        </div>
        <div>
          <label className={labelClass} htmlFor="crop">
            {l.crop}
          </label>
          <select id="crop" name="crop" className={fieldClass} defaultValue="">
            <option value="" disabled>
              {l.cropSelect}
            </option>
            {crops.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
        </div>
        <div>
          <label className={labelClass} htmlFor="size">
            {l.size}
          </label>
          <input id="size" name="greenhouse_size_ha" type="number" min="0" step="0.1" className={fieldClass} />
        </div>
      </div>

      <div className="mt-4">
        <label className={labelClass} htmlFor="message">
          {l.message}
        </label>
        <textarea
          id="message"
          name="message"
          rows={4}
          placeholder={l.messagePlaceholder}
          className={fieldClass}
        />
      </div>

      {status === "error" && (
        <p role="alert" className="mt-4 text-sm font-medium text-accent">
          {l.error}
        </p>
      )}

      <button
        type="submit"
        disabled={status === "sending"}
        className="mt-5 inline-flex w-full items-center justify-center rounded-lg bg-brand px-5 py-3 text-sm font-semibold text-white transition-colors hover:bg-brand-strong focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand focus-visible:ring-offset-2 focus-visible:ring-offset-surface disabled:cursor-not-allowed disabled:opacity-60 sm:w-auto"
      >
        {status === "sending" ? l.sending : l.submit}
      </button>
    </form>
  );
}
