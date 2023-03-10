import React from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import HomepageFeatures from "@site/src/components/HomepageFeatures";
import MDXContent from "@theme/MDXContent";

import styles from "./index.module.css";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx("hero hero--primary", styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link className="button button--secondary button--lg" to="/docs/">
            Start Linking 🔗
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  return (
    <MDXContent>
      <Layout title={`Home`} description="Document containing links to stackup">
        <HomepageHeader />
        <main>
          <HomepageFeatures />
        </main>
      </Layout>
    </MDXContent>
  );
}
