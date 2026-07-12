import portfolioData from "../data/portfolio-hq-founder.json";
import { PortfolioDashboard } from "./components/PortfolioDashboard";
import type { PortfolioData } from "./types";

export default function Home() {
  return <PortfolioDashboard data={portfolioData as PortfolioData} />;
}
