export type Trust = {
  level: string;
  label: string;
  reasons: string[];
};

export type ConsistencyIssue = {
  id: string;
  source: string;
  message: string;
};

export type Product = {
  name: string;
  state: string;
  nextAction: string;
  freshness: string;
  evidenceDate: string;
  dirty: boolean;
  dirtyCount: number;
};

export type Funnel = {
  id: string;
  name: string;
  tag: string;
  steps: [string, number][];
};

export type Workflow = {
  id: string;
  name: string;
  cadence: string;
  lastRan: string | null;
  how: string;
};

export type PortfolioData = {
  generatedAt: string;
  sources: Record<string, string | null>;
  trust: Trust;
  consistencyIssues: ConsistencyIssue[];
  command: { bestNextAction: string };
  products: Product[];
  numbers: {
    activation: {
      rows: Array<Record<string, string | boolean>>;
      note: string;
    };
    funnels: Funnel[];
  };
  clocks: Array<{
    date: string | null;
    when: string | null;
    what: string;
    state: string;
  }>;
  workflows: Workflow[];
  executive: {
    ceoReviewed: string | null;
    top3: Array<{ title: string; body: string }>;
  };
  growth: {
    lastGrowthReview: string | null;
    experiments: Array<Record<string, string>>;
  };
  models: {
    asOf: string | null;
    models: Array<{
      model: string;
      vendor: string;
      in: number;
      out: number;
      role: string;
      tier: string;
    }>;
    matrix: Array<{ task: string; primary: string; review: string }>;
  };
  usage: {
    generatedAt: string;
    windowDays: number;
    totalCostUsd: number;
    note: string;
  };
};
