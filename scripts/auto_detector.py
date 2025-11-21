import os

class ProjectTypeDetector:
    def detect_project_type(self, path):
        if not os.path.exists(path):
            return "general"
            
        files = os.listdir(path)
        
        # Web Development indicators
        if any(f in files for f in ['package.json', 'tsconfig.json', 'index.html', 'next.config.js']):
            return "development"
            
        # Data Analysis indicators
        if any(f in files for f in ['notebooks', 'data', 'pandas', 'analysis.ipynb']):
            return "data_analysis"
            
        # Research indicators
        if any(f in files for f in ['paper.tex', 'references.bib', 'experiment_results']):
            return "research"
            
        # Automation indicators
        if any(f in files for f in ['Makefile', 'Justfile', 'scripts', 'workflows']):
            return "automation"
            
        return "general"

if __name__ == "__main__":
    import sys
    detector = ProjectTypeDetector()
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(detector.detect_project_type(path))
