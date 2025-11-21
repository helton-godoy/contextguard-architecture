import yaml
import os

class ConfigGenerator:
    def __init__(self, template_dir):
        self.template_dir = template_dir
        
    def generate_config(self, project_type, output_path):
        template_file = os.path.join(self.template_dir, f"{project_type}-project.yaml")
        
        if not os.path.exists(template_file):
            # Fallback to general
            template_file = os.path.join(self.template_dir, "general-project.yaml")
            
        with open(template_file, 'r') as f:
            config = yaml.safe_load(f)
            
        # Add dynamic values or overrides here if needed
        config['generated_at'] = "auto-init"
        
        with open(output_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)
            
        print(f"Generated config for {project_type} at {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python config_generator.py <project_type> <output_path>")
        sys.exit(1)
        
    generator = ConfigGenerator(os.path.join(os.path.dirname(__file__), "../templates"))
    generator.generate_config(sys.argv[1], sys.argv[2])
