import puppeteer from "puppeteer";
import { baseUrl, formIds } from "./fakeform.js";
import dummyUser from "./dummy-data/dummyUser.js";

function getUserUrl({ baseUrl, formIds, userData }) {
  try {
    const parameters = Object.keys(formIds).reduce((acc, item) => {
      return acc + `entry.${formIds[item]}=${userData[item]}&`;
    }, "");
    // console.log("Link completo: " + baseUrl + parameters.slice(0, -1));
    return baseUrl + parameters.slice(0, -1); // slice to remove last '&' character
  } catch (error) {
    console.error("Error getting user url.", error);
  }
}

function clickButton({ page, type }) {
  let query;
  switch (type) {
    case "send":
      query = "Enviar";
      break;
    case "next":
      query = "Siguiente";
      break;
    default:
      console.error("Button type not supported");
  }

  const someFunction = (query) => {
    const someArray = [
      ...document.querySelectorAll('[role="button"] span span'),
    ];
    someArray
      .filter((element) => element.innerText.includes(query))[0]
      .parentNode.parentNode.click();
  };

  return page.evaluate(someFunction, query);
}

function sendUserForm(allData) {
  allData.map(async (userData) => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // 🔗 1. Get form url with user data filled in
    try {
      const userUrl = getUserUrl({ baseUrl, formIds, userData });
      await page.goto(userUrl, { waitUntil: "networkidle2" });
      await page.screenshot({ path: "src/screenshots/form1.png" });
    } catch {
      console.error("Error in step 1");
    }

    // ⏭ 2. Click the first 'next' button
    try {
      await clickButton({ page, type: "next" });
      await page.waitForNavigation({ waitUntil: "networkidle2" });
      await page.screenshot({ path: "src/screenshots/form2.png" });
    } catch (error) {
      console.error("Error in step 2", error);
    }

    // ⏭ 3. Click the second 'next' button
    try {
      await clickButton({ page, type: "next" });
      await page.waitForNavigation({ waitUntil: "networkidle2" });
      await page.screenshot({ path: "src/screenshots/form3.png" });
    } catch {
      console.error("Error in step 3");
    }

    try {
      if (
        userData.userType != "Administrativo" &&
        userData.userType != "Docente"
      ) {
        // ⏭ 4 Academic program section. (Estudiantes pregrado, posgrado y egresados). Click the third 'next' button
        await clickButton({ page, type: "next" });
        await page.waitForNavigation({ waitUntil: "networkidle2" });
        await page.screenshot({ path: "src/screenshots/form4.png" });
      }
    } catch {
      console.error("Error in step 4");
    }

    // ⏭ 5 Faculty section. (Administrativos y Docentes) Click the fifth 'next' button
    try {
      await clickButton({ page, type: "next" });
      await page.waitForNavigation({ waitUntil: "networkidle2" });
      await page.screenshot({ path: "src/screenshots/form5.png" });
    } catch {
      console.error("Error in step 5");
    }

    // ✅ 6 Final section: send the form. Click the 'send' button ->
    try {
      await clickButton({ page, type: "send" });
      await page.screenshot({ path: "src/screenshots/form5.png" });
    } catch {
      console.error("Error in step 6");
    }

    await browser.close();
  });
}

// 🏃‍♀️ Run the app here!
sendUserForm(dummyUser);
