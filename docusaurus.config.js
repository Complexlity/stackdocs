// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "StackDocs",
  tagline: "Linking You To All StackUp Campaigns!!",
  favicon: "img/favicon.ico",

  // Set the production url of your site here
  url: "https://stackdocs.netlify.app/",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },
  plugins: [
    [
      "content-docs",
      {
        id: "tracks",
        editCurrentVersion: true,
        path: "tracks",
        routeBasePath: "tracks",
        sidebarPath: require.resolve("./sidebarTracks.js"),
      },
    ],
  ],

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: "https://github.com/Complexlity/stackdocs",
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: "img/docusaurus-social-card.jpg",
      announcementBar: {
        id: "announcementBar-2",
        content: `⭐️ If you like StackDocs, give it a star on <a target="_blank" rel="noopener noreferrer" href="https://github.com/Complexlity/stackdocs">GitHub</a>`,
      },
      algolia: {
        // The application ID provided by Algolia
        appId: "WMWG4KXEJN",

        // Public API key: it is safe to commit it
        apiKey: "fdff565a4ca0bc7f7a30e8cb099198fa",

        indexName: "stackdocs",

        // Optional: see doc section below
        contextualSearch: true,

        // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
        externalUrlRegex: "external\\.com|domain\\.com",

        // Optional: Replace parts of the item URLs from Algolia. Useful when using the same search index for multiple deployments using a different baseUrl. You can use regexp or string in the `from` param. For example: localhost:3000 vs myCompany.com/docs
        replaceSearchResultPathname: {
          from: "/docs/", // or as RegExp: /\/docs\//
          to: "/",
        },

        // Optional: Algolia search parameters
        searchParameters: {},

        // Optional: path for search page that enabled by default (`false` to disable it)
        searchPagePath: "search",

        //... other Algolia params
      },
      navbar: {
        title: "StackDocs",
        logo: {
          alt: "Rocket Logo",
          src: "img/rocket.svg",
        },
        items: [
          {
            type: "doc",
            docId: "welcome",
            position: "left",
            label: "Campaigns",
          },
          { to: "/tracks/coming-soon", label: "Tracks", position: "left" },

          {
            href: "https://github.com/Complexlity/stackdocs",
            position: "right",
            className: "nav-github-link",
            "aria-label": "GitHub repository",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Docs",
            items: [
              {
                label: "Campaigns",
                to: "/docs",
              },
              {
                label: "Tracks",
                to: "/tracks/coming-soon",
              },
            ],
          },
          {
            title: "StackUp Community",
            items: [
              {
                label: "Discord",
                href: "https://bit.ly/3Qjl8Pk",
              },
              {
                label: "Twitter",
                href: "https://twitter.com/StackUpHQ?s=20",
              },
            ],
          },
        ],
        copyright: `<div>
            Copyright © ${new Date().getFullYear()}, Inc. Built By
            <a target="_blank" href="https://complexlity-personal-portfolio.netlify.app/">Complexlity</a>.
          </div>`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
