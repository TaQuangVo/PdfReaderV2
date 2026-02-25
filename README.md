# Flyttblankett Monitorering – Azure Function

En Azure Function App som automatiserar hanteringen av inkommande flyttblanketter via e-post.

## Vad gör systemet?

När ett e-postmeddelande med en bifogad PDF (flyttblankett) tas emot via en Azure Logic App, skickas PDF-filen till denna funktion som:

1. **Läser ut ISINs** från PDF-filen
2. **Identifierar depåinstitut** från PDF-texten
3. **Läser ut depånummer** från e-postens brödtext
4. **Väljer rätt e-postmall** baserat på depåinstitut och typ av ISIN
5. **Returnerar** mottagare, meddelande, ämnesrad och filnamn till Logic App:en som skickar vidare e-postmeddelandet

## Endpoints

### `POST /api/validate-isins`
Tar emot en PDF (base64-kodad) och en valfri `email_body`-frågeparameter med e-postens brödtext.

### `POST /api/validate-isins-CU`
Tar emot ett JSON-objekt från ett externt system istället för en PDF.

## Miljövariabler

| Variabel | Beskrivning |
|----------|-------------|
| `SKIP_ISIN_VALIDATION` | Sätt till `true` för att hoppa över ISIN-validering (används vid lokal testning) |

## Lokal körning

```bash
func start
```

Kräver `local.settings.json` med `FUNCTIONS_WORKER_RUNTIME` satt till `python`.
