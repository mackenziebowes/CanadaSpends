import { Label } from "@/components/label";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/tabs";
import { Textarea } from "@/components/textarea";

interface ChartTypesProps {
  dataTab: string;
  setDataTab: (tab: string) => void;
  dataText: string;
  setDataText: (text: string) => void;
  file: File | null;
  handleFileChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

export const ChartDataField = ({
  dataTab,
  setDataTab,
  dataText,
  setDataText,
  file,
  handleFileChange,
}: ChartTypesProps) => {
  return (
    <div className="flex flex-col gap-2">
      <Label htmlFor="chart-type">Chart Data</Label>
      <Tabs value={dataTab} onValueChange={setDataTab} className="w-full">
        <TabsList className="w-full mb-2 bg-muted">
          <TabsTrigger value="upload" className="flex-1">
            Upload File
          </TabsTrigger>
          <TabsTrigger value="paste" className="flex-1">
            Paste Data
          </TabsTrigger>
        </TabsList>
        <TabsContent value="upload">
          <label htmlFor="data-file" className="block text-sm font-medium mb-1">
            Upload CSV or JSON
          </label>
          <input
            id="data-file"
            type="file"
            accept=".csv,application/json"
            className="w-full text-sm"
            onChange={handleFileChange}
          />
          {file && (
            <div className="text-xs text-gray-500 mt-1 truncate">
              Selected: {file.name}
            </div>
          )}
        </TabsContent>
        <TabsContent value="paste">
          <label htmlFor="data-text" className="block text-sm font-medium mb-1">
            Paste Data (CSV or JSON)
          </label>
          <Textarea
            id="data-text"
            placeholder="Paste CSV or JSON data here"
            className="bg-background"
            value={dataText}
            onChange={(e) => setDataText(e.target.value)}
          />
        </TabsContent>
      </Tabs>
    </div>
  );
};
