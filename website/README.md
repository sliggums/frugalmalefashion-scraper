<h1 align="center">Bragging Bargains Website  </h1>



## Commands

### Run dev server

```shell
$ npm start
```

Run dev server on [http://localhost:8080](http://localhost:8080)

### Build

```shell
$ npm run build
```

Creating a Production Build. The build artifacts will be stored in the `dist/` directory.

### Deploy github pages

```json
# edit package.json
{
  ...
  "hompage": "https://{github username}.github.io/{repository name}",
}
```

```shell
$ npm run deploy
```

Deploy to github pages
