// TODO: change any to enum with type of page
// TODO: should return any contentType of page
export const getPagesProps = async (queryPage: any = "page") => {
  const cmsBaseUrl = import.meta.env.VITE_CMS_BASE;
  const pageDir = import.meta.env.VITE_CMS_PAGE;
  const pageUrl =`${cmsBaseUrl}${pageDir}`;

  const response = JSON.parse(await (await fetch(pageUrl)).text());
  // TODO: create the interface for entry
  const pages = response.items.map((entry: any) => ({
    params: { slug: entry.meta.slug },
    props: {
      title: entry.title,
      body: entry?.body,
    },
  }));

  // TODO: make a mapper for serialize the data

  return pages;
};
