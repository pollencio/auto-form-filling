import puppeteer from "puppeteer";
import { baseUrl, formIds } from "./constants.mjs";
import dummyUser from "./dummy-data/dummyUser.mjs";

function getUserUrl({ baseUrl, formIds, userData }) {
  const parameters = Object.keys(formIds).reduce((acc, item) => {
    return acc + `entry.${formIds[item]}=${userData[item]}&`;
  }, "");
  return baseUrl + parameters;
}

async function launchPuppeteer() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: "networkidle2" });
  await page.screenshot({ path: "src/screenshots/form.png" });
  await page.pdf({ path: "src/screenshots/form.pdf", format: "a4" });

  await browser.close();
}

console.log("----URL", baseUrl);
console.log("----FORM IDS", formIds);
console.log("----USER DATA", dummyUser);

console.log(getUserUrl(baseUrl, formIds, dummyUser));
