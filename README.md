# rowsapi

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install rowsapi
```
<!-- End SDK Installation -->

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## SDK Available Operations

### Spreadsheet

* `append_range_cells_by_spreadsheet_id` - Append values to range
* `get_range_cells_by_spreadsheet_id` - Get cells from range
* `get_range_values_by_spreadsheet_id` - Get values from range
* `get_spreadsheet_by_spreadsheet_id` - Get spreadsheet information
* `write_range_values_by_spreadsheet_id` - Overwrite cells in range

### Workspace

* `get_workspace_folders` - List folders
* `get_workspace_information` - Get workspace information
* `get_workspace_spreadsheets` - List spreadsheets

<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)