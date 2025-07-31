"use client";

import { H1, PageContent, Section } from "@/components/Layout";
import { Button } from "@/components/button";
import React, { useState } from "react";
import { ChartDataField, ChartTypeField, ChartPreview } from "./_components";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { parseCSV } from "@/utils/csvUtils";
import { Download, Share2 } from "lucide-react";
// For now, import the sample data as a string (in a real app, use dynamic import or fetch)
const sampleData = `Province,Financial Year,Ministry,Slug,Total Spending (B),Formatted Spending,Spending %,Formatted %\nOntario,2023-24,Health,health,73.361715876,$73.4B,36.56479580729396,36.6%\nOntario,2023-24,Education,education,39.73311054599999,$39.7B,19.803695381918086,19.8%\nOntario,2023-24,Children, Community and Social Services,children-community-and-social-services,19.620429025000007,$19.6B,9.779173951754979,9.8%\nOntario,2023-24,Finance,finance,13.559998414999999,$13.6B,6.758546569845292,6.8%\nOntario,2023-24,Transportation,transportation,12.073573912999997,$12.1B,6.017685921350437,6.0%\nOntario,2023-24,Long-Term Care,long-term-care,7.892942800999999,$7.9B,3.9339843458000607,3.9%\nOntario,2023-24,Colleges and Universities,colleges-and-universities,7.115984565000001,$7.1B,3.5467344169931305,3.5%\nOntario,2023-24,Energy,energy,6.035839838,$6.0B,3.008370899816987,3.0%\nOntario,2023-24,Solicitor General,solicitor-general,4.219737070999999,$4.2B,2.1031926873463473,2.1%\nOntario,2023-24,Attorney General,attorney-general,2.2176205340000004,$2.2B,1.1053018735389128,1.1%\nOntario,2023-24,Labour, Immigration, Training and Skills Development,labour-immigration-training-and-skills-development,1.9414598469999997,$1.9B,0.9676584309124504,1.0%\nOntario,2023-24,Municipal Affairs and Housing,municipal-affairs-and-housing,1.7765950109999997,$1.8B,0.8854868378388604,0.9%\nOntario,2023-24,Infrastructure,infrastructure,1.6423008580000005,$1.6B,0.8185522218211767,0.8%\nOntario,2023-24,Treasury Board Secretariat,treasury-board-secretariat,1.5068189329999995,$1.5B,0.7510255989218778,0.8%\nOntario,2023-24,Tourism, Culture, and Sport,tourism-culture-and-sport,1.4831634159999998,$1.5B,0.7392352647061002,0.7%\nOntario,2023-24,Economic Development, Job Creation and Trade,economic-development-job-creation-and-trade,1.2826329339999998,$1.3B,0.6392872735786601,0.6%\nOntario,2023-24,Public and Business Service Delivery,public-and-business-service-delivery,1.042719266,$1.0B,0.5197099957430859,0.5%\nOntario,2023-24,Natural Resources and Forestry,natural-resources-and-forestry,0.9687723630000002,$1.0B,0.48285353217090105,0.5%\nOntario,2023-24,Northern Development,northern-development,0.691513744,$0.7B,0.3446628605311733,0.3%\nOntario,2023-24,Agriculture, Food and Rural Affairs,agriculture-food-and-rural-affairs,0.627143398,$0.6B,0.31257952483721,0.3%\nOntario,2023-24,Mines,mines,0.5552162800000001,$0.6B,0.27672975835788577,0.3%\nOntario,2023-24,Environment, Conservation and Parks,environment-conservation-and-parks,0.492531089,$0.5B,0.24548633415921503,0.2%\nOntario,2023-24,Office of the Assembly,office-of-the-assembly,0.19565917200000002,$0.2B,0.09752004279857213,0.1%\nOntario,2023-24,Seniors and Accessibility,seniors-and-accessibility,0.171375024,$0.2B,0.08541638761042249,0.1%\nOntario,2023-24,Indigenous Affairs,indigenous-affairs,0.14656269400000002,$0.1B,0.07304947703424827,0.1%\nOntario,2023-24,Citizenship and Multiculturalism,citizenship-and-multiculturalism,0.08238444499999999,$0.1B,0.041061885932628855,0.0%\nOntario,2023-24,Office of the Chief Electoral Officer,office-of-the-chief-electoral-officer-office-of-the-chief-electoral-officer,0.065673155,$0.1B,0.03273267908093396,0.0%\nOntario,2023-24,Cabinet Office,cabinet-office-cabinet-office,0.06378201399999997,$0.1B,0.031790100466433144,0.0%\nOntario,2023-24,Ombudsman Ontario,ombudsman-ontario-ombudsman-ontario,0.028211491999999998,$0.0B,0.014061113921363087,0.0%\nOntario,2023-24,Office of the Auditor General,office-of-the-auditor-general-office-of-the-auditor-general,0.026668695000000003,$0.0B,0.013292156208153974,0.0%\nOntario,2023-24,Francophone Affairs,francophone-affairs-francophone-affairs,0.008025964,$0.0B,0.004000284498698579,0.0%\nOntario,2023-24,Office of the Premier,office-of-the-premier-office-of-the-premier,0.002410704999999999,$0.0B,0.001201538636659117,0.0%\nOntario,2023-24,Office of the Lieutenant Governor,office-of-the-lieutenant-governor-office-of-the-lieutenant-governor,0.0022568300000000005,$0.0B,0.0011248445750813131,0.0%`;

export default function DataVisualizerPage() {
  const [title, setTitle] = useState("My Chart");
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
          <H1>Data Visualizer</H1>
          <p className="text-lg text-gray-600 mt-4 max-w-3xl mx-auto">
            Create your own charts and graphs to visualize government data.
            Share and embed them on to your website, blog, or social media.
          </p>
        </div>
        <div className="flex flex-col md:flex-row gap-8">
          {/* Left column: Configuration (1/3) */}
          <div className="md:w-1/3 w-full bg-accent/50 p-4 rounded shadow-sm">
            <h2 className="text-xl font-semibold mb-4">Configuration</h2>
            <form className="flex flex-col gap-6">
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
          <div className="relative md:w-2/3 w-full bg-white p-4 rounded shadow min-h-[300px]">
            <div className="flex justify-between items-center">
              <h2 className="text-xl font-semibold mb-4">Preview</h2>
              <div>
                <Button
                  variant="ghost"
                  size="icon"
                  aria-label="Download chart"
                  onClick={() => {
                    // TODO: Implement download logic
                    alert("Download chart (not implemented)");
                  }}
                >
                  <Download className="w-5 h-5" />
                </Button>
                <Button
                  variant="ghost"
                  size="icon"
                  aria-label="Share chart"
                  onClick={() => {
                    // TODO: Implement share logic
                    alert("Share chart (not implemented)");
                  }}
                >
                  <Share2 className="w-5 h-5" />
                </Button>
              </div>
            </div>
            <ChartPreview
              chartType={chartType}
              title={title}
              data={parseCSV(sampleData)}
            />
          </div>
        </div>
      </Section>
    </PageContent>
  );
}
