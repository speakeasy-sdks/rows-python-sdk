<!-- Start SDK Example Usage -->
```python
import rowsapi
from rowsapi.models import operations, shared

s = rowsapi.Rowsapi()
s.config_security(
    security=shared.Security(
        bearer=shared.SchemeBearer(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    )
)
    
req = operations.AppendRangeCellsBySpreadsheetIDRequest(
    path_params=operations.AppendRangeCellsBySpreadsheetIDPathParams(
        range="sit",
        spreadsheet_id="voluptas",
        table_id="culpa",
    ),
    request=shared.AppendValues(
        values=[
            [
                "dolor",
                "expedita",
                "voluptas",
            ],
            [
                "et",
            ],
        ],
    ),
)
    
res = s.spreadsheet.append_range_cells_by_spreadsheet_id(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->