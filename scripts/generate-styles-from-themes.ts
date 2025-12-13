import { readFileSync, readdirSync } from "node:fs";
import { cwd } from "node:process";
import { join } from "node:path";

const styleFolder = join(cwd(), "src", "styles");
const coloursFolder = join(styleFolder, "colours");
// const chartsFolder = join(styleFolder, "charts");
// const themesFolder = join(styleFolder, "themes");

const getColourThemes = () => {
  const themeFiles = readdirSync(coloursFolder).filter((fileName) => {
    const notIndex = fileName !== "index.css";
    const isCss = fileName.endsWith(".css");
    return notIndex && isCss;
  });
  const themeFileContents: Record<string, Record<string, string>> = {};
  for (const file of themeFiles) {
    const themeName = file.slice(0, file.length - 4); // trim ".css";
    let lines = readFileSync(join(coloursFolder, file), "utf-8")
      .split("\n")
      .filter((line) => line.startsWith("  --color-"))
      .map((line) =>
        line
          .slice(0, line.length - 1)
          .trim()
          .slice(line.lastIndexOf("-") - 1, line.length),
      );
    const keyArray = lines.map((line) =>
      line.split(":").map((part) => part.trim()),
    );
    const themeObject: Record<string, string> = {};
    for (const key of keyArray) {
      themeObject[key[0]] = key[1];
    }
    themeFileContents[themeName] = themeObject;
  }
  return themeFileContents;
};

// const writeColourThemes = (themes: Record<string, Record<string, string>>) => {
//   for (const theme of Object.entries(themes)) {
//     console.dir({ theme }, { depth: null });
//     const outFile = join(coloursFolder, `${theme[0]}.ts`);
//     const outContents = `
// export const ${theme[0]} = ${JSON.stringify(theme[1])};`;
//     Bun.write(outFile, outContents);
//   }
// };

const main = () => {
  const colours = getColourThemes();
  console.dir({ colours });
  //   writeColourThemes(colours);
};

main();
