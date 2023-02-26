import React from "react";
import clsx from "clsx";
import styles from "./styles.module.css";

const FeatureList = [
  {
    title: "For Stackies",
    Svg: require("@site/static/img/for-stackies.svg").default,
    description: (
      <>
        StackDocs was designed from the ground up to help bring stackies closer
        to the platform.
      </>
    ),
  },
  {
    title: "Ease Of Access",
    Svg: require("@site/static/img/ease.svg").default,
    description: (
      <>
        StackDocs lets you access your preferred campaign or quest in a single
        click 👆. You also have access to all past campaigns and quests you may
        have missed
      </>
    ),
  },
  {
    title: "Powered by React",
    Svg: require("@site/static/img/search.svg").default,
    description: (
      <>
        Extend or customize your website layout by reusing React. Docusaurus can
        be extended while reusing the same header and footer.
      </>
    ),
  },
];

function Feature({ Svg, title, description }) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
