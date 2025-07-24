"use client";

import { H1, PageContent, Section } from "@/components/Layout";
import { Button } from "@/components/button";
import React, { useState } from "react";
import { ChartDataField } from "./_components/chart-data-field";
import { ChartTypeField } from "./_components/chart-type-field";
import { Input } from "@/components/input";
import { Label } from "@/components/label";

export default function ChartVisualizerPage() {
  const [title, setTitle] = useState("");
  const [chartType, setChartType] = useState("bar");
  const [dataText, setDataText] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [dataTab, setDataTab] = useState("upload");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  return (
    <PageContent>
      <Section>
        <div className="text-center mb-8">
          <H1>Chart Visualizer</H1>
          <p className="text-lg text-gray-600 mt-4 max-w-3xl mx-auto">
            Create your own charts and graphs to visualize government data.
            Share and embed them on to your website, blog, or social media.
          </p>
        </div>
        <div className="flex flex-col md:flex-row gap-8">
          {/* Left column: Configuration (1/3) */}
          <div className="md:w-1/3 w-full bg-accent/50 p-4 rounded shadow-sm">
            <h2 className="text-xl font-semibold mb-4">Configuration</h2>
            <form className="flex flex-col gap-4">
              {/* Chart Title */}
              <div className="flex flex-col gap-2">
                <Label htmlFor="chart-title">Chart Title</Label>
                <Input
                  id="chart-title"
                  type="text"
                  className="bg-background"
                  placeholder="Enter chart title"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                />
              </div>
              {/* Chart Type */}
              <ChartTypeField
                chartType={chartType}
                setChartType={setChartType}
              />
              {/* Data Input: Tabs for Upload and Paste */}
              <ChartDataField
                dataTab={dataTab}
                setDataTab={setDataTab}
                dataText={dataText}
                setDataText={setDataText}
                file={file}
                handleFileChange={handleFileChange}
              />
              {/* Parse Data Button */}
              <Button type="button" className="w-full mt-2">
                Parse Data
              </Button>
            </form>
          </div>
          {/* Right column: Chart Preview (2/3) */}
          <div className="md:w-2/3 w-full bg-white p-4 rounded shadow min-h-[300px]">
            <h2 className="text-xl font-semibold mb-4">Preview</h2>
            <div className="text-gray-400 italic">
              Chart preview will appear here
            </div>
          </div>
        </div>
      </Section>
    </PageContent>
  );
}
