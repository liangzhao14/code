export default function DataTable({ columns, rows, renderActions }) {
  return (
    <table>
      <thead>
        <tr>
          {columns.map((column) => (
            <th key={column.key}>{column.title}</th>
          ))}
          {renderActions ? <th>操作</th> : null}
        </tr>
      </thead>
      <tbody>
        {rows.map((row) => (
          <tr key={row.id || row.caseId || row.name}>
            {columns.map((column) => (
              <td key={column.key}>{column.render ? column.render(row) : row[column.key]}</td>
            ))}
            {renderActions ? <td><div className="table-actions">{renderActions(row)}</div></td> : null}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
