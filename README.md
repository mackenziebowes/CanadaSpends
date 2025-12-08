# Canada Spends 

We help Canadians understand how their governments spend their money.

A government cannot be held accountable if people don't understand what the government is doing. We aim to
bring transparency to every level of government in Canada: federal, provincial, municipal and school boards, public bodies, everyone.

## Wrapping your head around what governments do

It is challenging to evaluate what a government even does from the outside. Where do you even start?

Governments are huge and unwieldly creatures that even their leaders (the politicians) have a hard time getting a handle on things. Politicians have come up with systems to better guide what the public service does. The biggest way they do this is by establishing programs which have goals, constraints and funding attached to them. Some of these programs are statutory (they've written a law saying thou must spend this money. Think Old Age Security, or the Canada Child Benefit; no senior or family is hanging in the balance every year because politicians haven't approved the funding for it). There are also "voted" spending allocations which happen twice a year in the federal estimates. This funding 

Governments then go and create documentation about the effectiveness of these programs. 

Follow the money.


If  allocated money, and that money is getting spent (not the same thing!), then the government is prioritizing that, otherwise it is prioritizing something else. 

## Ambition

We bring this transparency in two ways:

1. We parse, aggregate and visualize audited financial statements that governments publish so that everyone can
   understand how their government spends their money and how it changes over time.
2. We aggregate and normalize government spending databases to make the data fast to search and accessible.

## Roadmap
### Audited Financial Statements 

- [ ] Automatically extract statements of operations and accumulated surplus from PDFs as JSON
- [ ] Create sankey diagrams from each of those statements. 
- [ ] Collect all audited financial statements from Canadian institutions. 

## Getting Started

Canada Spends is a NextJS app. To run it, run:

```
pnpm install
pnpm run dev
```

## Linting

This project uses ESLint with Next.js configuration. Run linting with:

```bash
pnpm lint          # Check for linting issues
pnpm lint:fix      # Auto-fix auto-fixable issues
```

The linting configuration enforces TypeScript best practices, React rules, and Next.js optimizations while keeping most issues as warnings (temporarily) to avoid blocking development.

## Prettier

This project uses [Prettier](https://prettier.io/) for code formatting. To format your code manually, run:

```bash
pnpm format
```

## Git Hooks

This project automatically runs linting checks and formatting before each commit using `simple-git-hooks`. This is enabled automatically when you run `pnpm install`. If you need to enable it manually:

```bash
npx simple-git-hooks
```

If linting fails, the commit will be blocked until issues are resolved.
