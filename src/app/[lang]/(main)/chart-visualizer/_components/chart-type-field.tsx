import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";
import { BarChart, LineChart, PieChart, ScatterChart } from "lucide-react";
import { Label } from "@/components/ui/label";

const chartTypes = [
  { label: "Bar Chart", value: "bar", icon: BarChart },
  { label: "Line Chart", value: "line", icon: LineChart },
  { label: "Pie Chart", value: "pie", icon: PieChart },
  { label: "Scatter Plot", value: "scatter", icon: ScatterChart },
];

export function ChartTypeField({
  chartType,
  setChartType,
}: {
  chartType: string;
  setChartType: (chartType: string) => void;
}) {
  return (
    <div className="flex flex-col gap-2">
      <Label>Chart Type</Label>
      <ToggleGroup
        type="single"
        value={chartType}
        onValueChange={setChartType}
        className="grid grid-cols-2 gap-3 rounded-none w-full"
      >
        {chartTypes.map((type) => {
          const Icon = type.icon;
          return (
            <ToggleGroupItem
              key={type.value}
              value={type.value}
              className="flex justify-start items-center gap-2 text-default font-normal border data-[state=on]:bg-primary data-[state=on]:text-white data-[state=on]:border-primary data-[state=off]:bg-white data-[state=off]:text-black data-[state=off]:border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary rounded-sm first:rounded-sm last:rounded-sm cursor-pointer"
            >
              <Icon className="w-6 h-6" />
              {type.label}
            </ToggleGroupItem>
          );
        })}
      </ToggleGroup>
    </div>
  );
}
