import React from "react";
import { BarChart as BarChartComponent } from "@/components/BarChart";
import { LineChart as LineChartComponent } from "@/components/LineChart";
import {
  PieChart as RechartsPieChart,
  Pie,
  Cell,
  Tooltip as RechartsTooltip,
  ResponsiveContainer,
  ScatterChart as RechartsScatterChart,
  Scatter,
  XAxis,
  YAxis,
  CartesianGrid,
} from "recharts";
import { H3 } from "@/components/Layout";

const COLORS = ["#2563eb", "#f59e42", "#10b981", "#e11d48"];

type ChartData = Record<string, unknown>;

type ChartPreviewProps = {
  chartType: string;
  title: string;
  data: ChartData[];
};

export function ChartPreview({ chartType, title, data }: ChartPreviewProps) {
  const hasKey = (arr: ChartData[], key: string) =>
    Array.isArray(arr) && arr.length > 0 && arr[0][key] !== undefined;

  return (
    <div>
      <H3>{title}</H3>
      <div className="h-80 w-full">
        {chartType === "bar" &&
        hasKey(data, "Ministry") &&
        hasKey(data, "Total Spending (B)") ? (
          <BarChartComponent
            data={data}
            index="Ministry"
            categories={["Total Spending (B)"]}
            showLegend={true}
            showGridLines={true}
          />
        ) : chartType === "bar" ? (
          <pre className="text-xs text-gray-500 bg-gray-100 p-2 rounded">
            {JSON.stringify(data, null, 2)}
          </pre>
        ) : null}
        {chartType === "line" &&
        hasKey(data, "Ministry") &&
        hasKey(data, "Total Spending (B)") ? (
          <LineChartComponent
            data={data}
            index="Ministry"
            categories={["Total Spending (B)"]}
            showLegend={true}
            showGridLines={true}
          />
        ) : chartType === "line" ? (
          <pre className="text-xs text-gray-500 bg-gray-100 p-2 rounded">
            {JSON.stringify(data, null, 2)}
          </pre>
        ) : null}
        {chartType === "pie" &&
        hasKey(data, "Ministry") &&
        hasKey(data, "Total Spending (B)") ? (
          <ResponsiveContainer width="100%" height="100%">
            <RechartsPieChart>
              <RechartsTooltip />
              <Pie
                data={data}
                dataKey="Total Spending (B)"
                nameKey="Ministry"
                cx="50%"
                cy="50%"
                outerRadius={80}
                fill="#8884d8"
                label
              >
                {data.map((entry, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={COLORS[index % COLORS.length]}
                  />
                ))}
              </Pie>
            </RechartsPieChart>
          </ResponsiveContainer>
        ) : chartType === "pie" ? (
          <pre className="text-xs text-gray-500 bg-gray-100 p-2 rounded">
            {JSON.stringify(data, null, 2)}
          </pre>
        ) : null}
        {chartType === "scatter" && hasKey(data, "x") && hasKey(data, "y") ? (
          <ResponsiveContainer width="100%" height="100%">
            <RechartsScatterChart>
              <CartesianGrid />
              <XAxis dataKey="x" type="number" />
              <YAxis dataKey="y" type="number" />
              <RechartsTooltip cursor={{ strokeDasharray: "3 3" }} />
              <Scatter data={data} fill="#2563eb" />
            </RechartsScatterChart>
          </ResponsiveContainer>
        ) : chartType === "scatter" ? (
          <pre className="text-xs text-gray-500 bg-gray-100 p-2 rounded">
            {JSON.stringify(data, null, 2)}
          </pre>
        ) : null}
      </div>
    </div>
  );
}
