import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Textarea } from "@/components/ui/textarea";

interface ChartTypesProps {
  dataTab: string;
  setDataTab: (tab: string) => void;
  dataText: string;
  setDataText: (text: string) => void;
  handleFileChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

export function ChartDataField({
  dataTab,
  setDataTab,
  dataText,
  setDataText,
  handleFileChange,
}: ChartTypesProps) {
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
          <Label htmlFor="data-file" className="mb-2">
            Upload CSV or JSON
          </Label>
          <Input
            id="data-file"
            type="file"
            accept=".csv,application/json"
            className="bg-background"
            onChange={handleFileChange}
          />
        </TabsContent>
        <TabsContent value="paste">
          <Label htmlFor="data-text" className="mb-2">
            Paste Data (CSV or JSON)
          </Label>
          <Textarea
            id="data-text"
            placeholder="Paste CSV or JSON data here"
            className="bg-background h-24 resize-none"
            value={dataText}
            onChange={(e) => setDataText(e.target.value)}
          />
        </TabsContent>
      </Tabs>
    </div>
  );
}
