#!/usr/bin/env python3
"""
Digital Nomad Developer Kit - Packing List Generator
A smart packing list generator based on trip parameters and modular organization.
"""

import argparse
from datetime import datetime
from typing import Dict, List, Set
import json


class PackingListGenerator:
    """Generate optimized packing lists for digital nomads"""
    
    def __init__(self):
        self.base_items = {
            'tech': [
                'Laptop',
                'Laptop Charger',
                'Phone',
                'Phone Charging Cable',
                'Headphones',
                'Power Bank'
            ],
            'edc': [
                'Wallet',
                'Keys',
                'Notebook',
                'Pen',
                'Water Bottle'
            ]
        }
        
        self.module_mapping = {
            'tech': 'CoilCrate Case',
            'edc': 'KeyBit Pouch',
            'clothing': 'PackLite Combo (Flat/Cube)',
            'toiletries': 'DripDry Case'
        }
        
    def calculate_clothing(self, duration: int, capsule: bool = False) -> List[str]:
        """Calculate clothing items based on trip duration"""
        if duration <= 1:
            return []
        elif duration <= 3:
            return [
                '1-2 Shirts',
                '1 Pants',
                '2-3 Underwear',
                '2-3 Socks',
                '1 Sleepwear'
            ]
        else:
            base_clothing = [
                '3-5 Shirts (mix casual/work)',
                '2 Pants',
                '5-7 Underwear',
                '5-7 Socks',
                '1-2 Sleepwear',
                '1 Light Jacket'
            ]
            if capsule:
                base_clothing.extend([
                    '1 Athletic Wear Set',
                    '1 Smart Casual Outfit'
                ])
            return base_clothing
    
    def get_toiletries(self, duration: int) -> List[str]:
        """Get toiletries based on trip duration"""
        if duration <= 1:
            return []
        elif duration <= 3:
            return [
                'Travel-size Toothpaste',
                'Toothbrush',
                'Travel Shampoo/Soap',
                'Deodorant',
                'Basic Skincare'
            ]
        else:
            return [
                'Full-size Toiletries',
                'Toothbrush & Toothpaste',
                'Shampoo & Conditioner',
                'Body Wash',
                'Deodorant',
                'Skincare Products',
                'Medications',
                'First Aid Kit',
                'Sunscreen'
            ]
    
    def get_work_gear(self, work_intensity: str, duration: int) -> List[str]:
        """Get work-related gear based on intensity"""
        work_items = []
        
        if work_intensity in ['medium', 'heavy']:
            work_items.extend([
                'USB-C Hub/Adapter',
                'HDMI Cable',
                'External Mouse',
                'Laptop Stand (portable)'
            ])
        
        if work_intensity == 'heavy' or duration > 7:
            work_items.extend([
                'External Keyboard',
                'Second Monitor Cable',
                'Webcam (if needed)',
                'Microphone (if needed)'
            ])
        
        return work_items
    
    def get_base_pack_recommendation(self, trip_type: str, duration: int) -> Dict[str, str]:
        """Recommend base pack based on trip parameters"""
        if trip_type == 'commute' or duration <= 1:
            return {
                'pack': 'Today Shift 16L II',
                'url': 'https://fikacarry.com/products/today-shift-16l-ii',
                'capacity': '16L'
            }
        elif trip_type == 'weekend' or duration <= 3:
            return {
                'pack': 'Week Go 16L/22L',
                'url': 'https://fikacarry.com/products/week-go-16l-22l',
                'capacity': '16L-22L'
            }
        else:
            return {
                'pack': 'Week Go 22L',
                'url': 'https://fikacarry.com/products/week-go-16l-22l',
                'capacity': '22L'
            }
    
    def generate_packing_list(
        self, 
        trip_type: str, 
        duration: int, 
        work_intensity: str = 'medium',
        include_extras: bool = False
    ) -> Dict[str, any]:
        """
        Generate complete packing list
        
        Args:
            trip_type: 'commute' | 'weekend' | 'nomad'
            duration: Number of days
            work_intensity: 'light' | 'medium' | 'heavy'
            include_extras: Include optional items
        
        Returns:
            Dictionary with categorized packing list
        """
        packing_list = {
            'trip_info': {
                'type': trip_type,
                'duration': f"{duration} day(s)",
                'work_intensity': work_intensity,
                'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            },
            'recommended_pack': self.get_base_pack_recommendation(trip_type, duration),
            'items': {},
            'modules': [],
            'total_items': 0
        }
        
        # Base items (always included)
        packing_list['items']['Tech Essentials'] = self.base_items['tech'].copy()
        packing_list['items']['EDC (Everyday Carry)'] = self.base_items['edc'].copy()
        packing_list['modules'].extend(['CoilCrate Case', 'KeyBit Pouch'])
        
        # Work gear
        work_gear = self.get_work_gear(work_intensity, duration)
        if work_gear:
            packing_list['items']['Work Gear'] = work_gear
        
        # Clothing
        clothing = self.calculate_clothing(duration, capsule=(trip_type == 'nomad'))
        if clothing:
            packing_list['items']['Clothing'] = clothing
            packing_list['modules'].append('PackLite Combo Flat 4P')
            packing_list['modules'].append('PackLite Combo Cube 4P')
        
        # Toiletries
        toiletries = self.get_toiletries(duration)
        if toiletries:
            packing_list['items']['Toiletries & Health'] = toiletries
            packing_list['modules'].append('DripDry Case')
        
        # Long-term nomad extras
        if trip_type == 'nomad' or duration > 7:
            packing_list['items']['Travel Essentials'] = [
                'Universal Travel Adapter',
                'Packable Daypack',
                'E-Reader/Books',
                'Travel Documents',
                'Backup Credit Card'
            ]
        
        # Optional extras
        if include_extras:
            packing_list['items']['Optional Extras'] = [
                'Camera',
                'Portable Speaker',
                'Travel Pillow',
                'Eye Mask & Earplugs',
                'Reusable Shopping Bag'
            ]
        
        # Calculate total items
        total = sum(len(items) for items in packing_list['items'].values())
        packing_list['total_items'] = total
        
        # Remove duplicates from modules
        packing_list['modules'] = list(set(packing_list['modules']))
        
        return packing_list
    
    def print_packing_list(self, packing_list: Dict, format: str = 'text'):
        """Print packing list in specified format"""
        if format == 'json':
            print(json.dumps(packing_list, indent=2))
            return
        
        # Text format
        print("\n" + "="*60)
        print("🎒 DIGITAL NOMAD PACKING LIST")
        print("="*60)
        
        # Trip info
        info = packing_list['trip_info']
        print(f"\n📋 Trip Details:")
        print(f"   Type: {info['type'].upper()}")
        print(f"   Duration: {info['duration']}")
        print(f"   Work Intensity: {info['work_intensity'].upper()}")
        print(f"   Generated: {info['generated_at']}")
        
        # Recommended pack
        pack = packing_list['recommended_pack']
        print(f"\n🎒 Recommended Base Pack:")
        print(f"   {pack['pack']} ({pack['capacity']})")
        print(f"   {pack['url']}")
        
        # Modules
        print(f"\n📦 Required Modules:")
        for module in packing_list['modules']:
            print(f"   ✓ {module}")
        
        # Items by category
        print(f"\n📝 Packing List ({packing_list['total_items']} items):")
        print("-"*60)
        
        for category, items in packing_list['items'].items():
            print(f"\n{category}:")
            for item in items:
                print(f"   [ ] {item}")
        
        print("\n" + "="*60)
        print("💡 Tip: Check off items as you pack them!")
        print("🔗 Shop FIKA CARRY: https://fikacarry.com")
        print("="*60 + "\n")
    
    def export_markdown(self, packing_list: Dict, filename: str = None):
        """Export packing list as Markdown checklist"""
        if filename is None:
            filename = f"packing-list-{datetime.now().strftime('%Y%m%d')}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# 🎒 Digital Nomad Packing List\n\n")
            
            # Trip info
            info = packing_list['trip_info']
            f.write("## 📋 Trip Details\n\n")
            f.write(f"- **Type:** {info['type'].upper()}\n")
            f.write(f"- **Duration:** {info['duration']}\n")
            f.write(f"- **Work Intensity:** {info['work_intensity'].upper()}\n")
            f.write(f"- **Generated:** {info['generated_at']}\n\n")
            
            # Recommended pack
            pack = packing_list['recommended_pack']
            f.write("## 🎒 Recommended Base Pack\n\n")
            f.write(f"**[{pack['pack']}]({pack['url']})** ({pack['capacity']})\n\n")
            
            # Modules
            f.write("## 📦 Required Modules\n\n")
            for module in packing_list['modules']:
                f.write(f"- ✓ {module}\n")
            f.write("\n")
            
            # Items
            f.write(f"## 📝 Packing Checklist ({packing_list['total_items']} items)\n\n")
            
            for category, items in packing_list['items'].items():
                f.write(f"### {category}\n\n")
                for item in items:
                    f.write(f"- [ ] {item}\n")
                f.write("\n")
            
            f.write("---\n\n")
            f.write("💡 **Tip:** Check off items as you pack them!\n\n")
            f.write("🔗 **Shop FIKA CARRY:** https://fikacarry.com\n")
        
        print(f"✅ Packing list exported to: {filename}")


def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description='Generate smart packing lists for digital nomads',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Daily commute
  python packing-list-generator.py --type commute --duration 1
  
  # Weekend workshop
  python packing-list-generator.py --type weekend --duration 3 --work-intensity heavy
  
  # Long-term nomad trip
  python packing-list-generator.py --type nomad --duration 14 --extras
  
  # Export as Markdown
  python packing-list-generator.py --type nomad --duration 7 --export packing.md
        """
    )
    
    parser.add_argument(
        '--type',
        choices=['commute', 'weekend', 'nomad'],
        required=True,
        help='Type of trip'
    )
    
    parser.add_argument(
        '--duration',
        type=int,
        required=True,
        help='Trip duration in days'
    )
    
    parser.add_argument(
        '--work-intensity',
        choices=['light', 'medium', 'heavy'],
        default='medium',
        help='Work intensity level (default: medium)'
    )
    
    parser.add_argument(
        '--extras',
        action='store_true',
        help='Include optional extra items'
    )
    
    parser.add_argument(
        '--format',
        choices=['text', 'json'],
        default='text',
        help='Output format (default: text)'
    )
    
    parser.add_argument(
        '--export',
        type=str,
        metavar='FILENAME',
        help='Export as Markdown checklist to specified file'
    )
    
    args = parser.parse_args()
    
    # Generate packing list
    generator = PackingListGenerator()
    packing_list = generator.generate_packing_list(
        trip_type=args.type,
        duration=args.duration,
        work_intensity=args.work_intensity,
        include_extras=args.extras
    )
    
    # Output
    if args.export:
        generator.export_markdown(packing_list, args.export)
    else:
        generator.print_packing_list(packing_list, args.format)


if __name__ == '__main__':
    main()
