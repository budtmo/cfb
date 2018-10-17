#!/usr/bin/env node

const chalk = require("chalk");
const figlet = require("figlet");
const program = require("commander")

program
  .version('0.0.1', '-v, --version')

program
  .command('write <text>')
  .alias('w')
  .description('Print out given text to console')
  .action(function (text) {
    console.log(
      chalk.green(
        figlet.textSync(text, {
          font: "Ghost",
          horizontalLayout: "default",
          verticalLayout: "default"
        })
      )
    );
  });

program.parse(process.argv);
