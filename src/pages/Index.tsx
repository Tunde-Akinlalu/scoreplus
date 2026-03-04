import { useState } from "react";
import { FileText, Download, Database, Users, Trophy, Table, FileSpreadsheet, FileDown } from "lucide-react";

const files = [
  { name: "app.py", desc: "Main Flask application with all routes (auth, events, scoring, export)", lines: 300 },
  { name: "config.py", desc: "Database & app configuration", lines: 14 },
  { name: "models.py", desc: "SQLAlchemy models (User, Event, Category, School, Athlete, Score)", lines: 95 },
  { name: "forms.py", desc: "Flask-WTF forms for all input interfaces", lines: 60 },
  { name: "requirements.txt", desc: "Python dependencies (Flask, SQLAlchemy, openpyxl, reportlab)", lines: 13 },
  { name: ".env.example", desc: "Environment variables template", lines: 5 },
  { name: "templates/base.html", desc: "Base template with ISGA branding (purple/cyan theme)", lines: 80 },
  { name: "templates/index.html", desc: "Home page with event listing", lines: 40 },
  { name: "templates/login.html", desc: "Login page", lines: 30 },
  { name: "templates/register.html", desc: "Registration page", lines: 35 },
  { name: "templates/score_input.html", desc: "Score entry with live auto-calculation", lines: 85 },
  { name: "templates/view_category.html", desc: "Full results table matching your CSV format", lines: 90 },
  { name: "templates/view_event.html", desc: "Event detail with categories", lines: 55 },
  { name: "templates/schools.html", desc: "School management page", lines: 30 },
];

const features = [
  { icon: Users, title: "User Login & Registration", desc: "Admin, scorer, viewer roles with Flask-Login" },
  { icon: Trophy, title: "Event & Category Management", desc: "Create events with 5-Piece / 4-Piece categories" },
  { icon: Table, title: "Score Input Interface", desc: "Real-time auto-calculation as you type scores" },
  { icon: Database, title: "MySQL Database", desc: "Full schema with SQLAlchemy ORM & Flask-Migrate" },
  { icon: FileSpreadsheet, title: "Export to Excel", desc: "Branded .xlsx with ISGA purple/cyan styling" },
  { icon: FileDown, title: "Export to PDF", desc: "Professional PDF reports with ReportLab" },
];

const Index = () => {
  const [activeTab, setActiveTab] = useState<"overview" | "setup" | "files">("overview");

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="bg-gradient-to-r from-[hsl(280,45%,33%)] to-[hsl(187,100%,42%)] text-white py-8">
        <div className="container mx-auto px-4 text-center">
          <div className="flex items-center justify-center gap-3 mb-4">
            <img
              src="https://www.isgagymnastics.org/wp-content/themes/accelerate/images/logo.png"
              alt="ISGA Logo"
              className="h-16"
              onError={(e) => { (e.target as HTMLImageElement).style.display = 'none'; }}
            />
            <h1 className="text-4xl font-bold">ISGA Scoring System</h1>
          </div>
          <p className="text-xl opacity-90">
            Flask + MySQL Application — Ready for PyCharm
          </p>
          <p className="mt-2 opacity-75">
            Complete scoring system matching your CSV sheet format with auto-calculations, exports & ISGA branding
          </p>
        </div>
      </header>

      <div className="container mx-auto px-4 py-8 max-w-5xl">
        {/* Tabs */}
        <div className="flex gap-1 mb-8 bg-muted rounded-lg p-1">
          {(["overview", "setup", "files"] as const).map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors capitalize ${
                activeTab === tab
                  ? "bg-background text-foreground shadow-sm"
                  : "text-muted-foreground hover:text-foreground"
              }`}
            >
              {tab}
            </button>
          ))}
        </div>

        {activeTab === "overview" && (
          <div>
            <h2 className="text-2xl font-bold text-foreground mb-6">Features</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
              {features.map((f, i) => (
                <div key={i} className="border border-border rounded-xl p-5 bg-card">
                  <f.icon className="h-8 w-8 mb-3" style={{ color: '#6B2D7B' }} />
                  <h3 className="font-semibold text-foreground">{f.title}</h3>
                  <p className="text-sm text-muted-foreground mt-1">{f.desc}</p>
                </div>
              ))}
            </div>

            <div className="border border-border rounded-xl p-6 bg-card">
              <h3 className="font-semibold text-lg mb-3 text-foreground">Scoring Logic (matches your CSV)</h3>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li>• <strong>Individual Total</strong> = Set Vault + Vol Vault + Set Floor + Vol Floor</li>
                <li>• <strong>Team Totals</strong> = Top 4 scores per apparatus across 6 athletes</li>
                <li>• <strong>Group Score</strong> = Sum of apparatus averages</li>
                <li>• <strong>Positions</strong> = Ranked across all teams in category</li>
                <li>• <strong>Dynamic rows</strong> = Add/remove athletes per school on the fly</li>
              </ul>
            </div>
          </div>
        )}

        {activeTab === "setup" && (
          <div className="space-y-6">
            <div className="border border-border rounded-xl p-6 bg-card">
              <h3 className="font-semibold text-lg mb-4 text-foreground">PyCharm Setup Guide</h3>
              <ol className="space-y-4 text-sm text-muted-foreground">
                <li className="flex gap-3">
                  <span className="font-bold text-foreground min-w-[24px]">1.</span>
                  <div>
                    <strong className="text-foreground">Create MySQL Database:</strong>
                    <pre className="bg-muted p-3 rounded-md mt-2 overflow-x-auto text-xs">
{`CREATE DATABASE isga_gymnastics 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;`}
                    </pre>
                  </div>
                </li>
                <li className="flex gap-3">
                  <span className="font-bold text-foreground min-w-[24px]">2.</span>
                  <div>
                    <strong className="text-foreground">Copy the <code>flask_app/</code> folder</strong> from this project to your local machine
                  </div>
                </li>
                <li className="flex gap-3">
                  <span className="font-bold text-foreground min-w-[24px]">3.</span>
                  <div>
                    <strong className="text-foreground">Open in PyCharm:</strong> File → Open → select the folder
                  </div>
                </li>
                <li className="flex gap-3">
                  <span className="font-bold text-foreground min-w-[24px]">4.</span>
                  <div>
                    <strong className="text-foreground">Install dependencies:</strong>
                    <pre className="bg-muted p-3 rounded-md mt-2 overflow-x-auto text-xs">{`pip install -r requirements.txt`}</pre>
                  </div>
                </li>
                <li className="flex gap-3">
                  <span className="font-bold text-foreground min-w-[24px]">5.</span>
                  <div>
                    <strong className="text-foreground">Configure .env:</strong>
                    <pre className="bg-muted p-3 rounded-md mt-2 overflow-x-auto text-xs">
{`cp .env.example .env
# Edit DATABASE_URL with your MySQL credentials`}
                    </pre>
                  </div>
                </li>
                <li className="flex gap-3">
                  <span className="font-bold text-foreground min-w-[24px]">6.</span>
                  <div>
                    <strong className="text-foreground">Run:</strong> Right-click <code>app.py</code> → Run, then open <code>http://localhost:5000</code>
                    <br />
                    <span className="text-xs">Default login: <strong>admin / admin123</strong></span>
                  </div>
                </li>
              </ol>
            </div>
          </div>
        )}

        {activeTab === "files" && (
          <div>
            <h2 className="text-2xl font-bold text-foreground mb-4">Generated Files</h2>
            <p className="text-muted-foreground mb-6 text-sm">
              All files are in the <code className="bg-muted px-2 py-1 rounded">flask_app/</code> directory. 
              Download them via GitHub or copy from the code editor.
            </p>
            <div className="space-y-2">
              {files.map((f, i) => (
                <div key={i} className="flex items-center gap-3 border border-border rounded-lg p-3 bg-card">
                  <FileText className="h-5 w-5 flex-shrink-0" style={{ color: '#00BCD4' }} />
                  <div className="flex-1 min-w-0">
                    <code className="text-sm font-medium text-foreground">{f.name}</code>
                    <p className="text-xs text-muted-foreground truncate">{f.desc}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Index;
