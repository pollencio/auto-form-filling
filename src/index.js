import puppeteer from "puppeteer";
import { baseUrl, formIds } from "./fakeform.js";
import dummyUser from "./dummy-data/dummyUser.js";

function getUserUrl({ baseUrl, formIds, userData }) {
  try {
    const parameters = Object.keys(formIds).reduce((acc, item, index) => {
      return acc + `entry.${formIds[item]}=${userData[item]}&`;
    }, "");
    console.log("Link completo: " + baseUrl + parameters.slice(0, -1));
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

  return page.evaluate(
    (query) =>
      [
        ...document.querySelectorAll(
          "span.appsMaterialWizButtonPaperbuttonLabel"
        ),
      ]
        .filter((element) => element.innerText.includes(query))[0]
        .parentNode.parentNode.click(),
    query
  );
}

async function sendUserForm(userData) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // 🔗 1. Get form url with user data filled in
  const userUrl = getUserUrl({ baseUrl, formIds, userData });
  await page.goto(userUrl, { waitUntil: "networkidle2" });
  await page.screenshot({ path: "src/screenshots/form1.png" });
 
  // ⏭ 2. Click the first 'next' button
  await clickButton({ page, type: "next" });
  await page.waitForNavigation({ waitUntil: "networkidle2" });
  await page.screenshot({ path: "src/screenshots/form2.png" });

  // ⏭ 3. Click the second 'next' button
  await clickButton({ page, type: "next" });
  await page.waitForNavigation({ waitUntil: "networkidle2" });
  await page.screenshot({ path: "src/screenshots/form3.png" });

  if (userData.userType != "Administrativo" && userData.userType != "Docente") {
    // ⏭ 4 Academic program section. (Estudiantes pregrado, posgrado y egresados). Click the third 'next' button
    await clickButton({ page, type: "next" });
    await page.waitForNavigation({ waitUntil: "networkidle2" });
    await page.screenshot({ path: "src/screenshots/form4.png" });
  }

  // ⏭ 5 Faculty section. (Administrativos y Docentes) Click the fifth 'next' button
  await clickButton({ page, type: "next" });
  await page.waitForNavigation({ waitUntil: "networkidle2" });
  await page.screenshot({ path: "src/screenshots/form5.png" });

  // ✅ 6 Final section: send the form. Click the 'send' button -> 
  await clickButton({ page, type: "send" });
  await page.screenshot({ path: "src/screenshots/form5.png" });


  await browser.close();
}

// 🏃‍♀️ Run the app here!
sendUserForm(dummyUser);