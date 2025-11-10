"""
Tests for the Unified Orb System

These tests validate that all components are integrated and work as a cohesive whole.
"""

import pytest
import numpy as np
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from orb_core import UnifiedOrb, get_orb, orb_process, OrbState, HyperStateTensor


class TestOrbInitialization:
    """Test Orb initialization and setup"""
    
    def test_orb_initializes(self):
        """Test that Orb initializes properly"""
        orb = UnifiedOrb()
        assert orb.state == OrbState.RESONATING
        assert orb.orb_signature is not None
        assert len(orb.orb_signature) > 0
    
    def test_quantum_registers_initialized(self):
        """Test quantum registers are set up"""
        orb = UnifiedOrb()
        assert len(orb.hyper_state.quantum_registers) == 64
        assert all(isinstance(q, complex) for q in orb.hyper_state.quantum_registers)
    
    def test_neural_lattice_initialized(self):
        """Test neural network lattice is set up"""
        orb = UnifiedOrb()
        assert orb.hyper_state.neural_weights.shape == (128, 128)
    
    def test_singleton_pattern(self):
        """Test that get_orb returns the same instance"""
        orb1 = get_orb()
        orb2 = get_orb()
        assert orb1 is orb2


class TestUnifiedInputProcessing:
    """Test unified input handling"""
    
    def test_text_query_processing(self):
        """Test processing of text queries"""
        orb = UnifiedOrb()
        result = orb.process("What is the weather today?")
        
        assert result['orb_signature'] == orb.orb_signature
        assert 'unified_result' in result
        assert result['provenance'] == 'all_sources_simultaneously'
    
    def test_code_snippet_processing(self):
        """Test processing of code snippets"""
        orb = UnifiedOrb()
        code = "def hello(): return 'world'"
        result = orb.process(code)
        
        assert 'unified_result' in result
        unified = result['unified_result']
        assert 'code_processing' in unified
        assert unified['code_processing']['python'] == 'parsed'
    
    def test_javascript_processing(self):
        """Test JavaScript code processing"""
        orb = UnifiedOrb()
        js_code = "function test() { return true; }"
        result = orb.process(js_code)
        
        unified = result['unified_result']
        assert 'code_processing' in unified
        assert unified['code_processing']['javascript'] == 'parsed'
    
    def test_terminal_command_processing(self):
        """Test terminal command processing"""
        orb = UnifiedOrb()
        result = orb.process("ls -la")
        
        unified = result['unified_result']
        assert 'terminal_orchestration' in unified
        assert unified['terminal_orchestration']['terminal_active'] is True
    
    def test_api_url_processing(self):
        """Test API/web URL processing"""
        orb = UnifiedOrb()
        result = orb.process("https://api.example.com/data")
        
        unified = result['unified_result']
        assert 'search_tools' in unified
    
    def test_binary_data_processing(self):
        """Test binary data processing"""
        orb = UnifiedOrb()
        result = orb.process("101010110101")
        
        unified = result['unified_result']
        # Should detect as binary
        assert 'quantum_computation' in unified
    
    def test_structured_data_processing(self):
        """Test structured data (dict) processing"""
        orb = UnifiedOrb()
        data = {"key": "value", "number": 42}
        result = orb.process(data)
        
        assert 'unified_result' in result
        assert result['unity_score'] > 0


class TestComponentIntegration:
    """Test that all components are integrated and working together"""
    
    def test_all_components_present(self):
        """Test all required components are in the result"""
        orb = UnifiedOrb()
        result = orb.process("test input")
        
        unified = result['unified_result']
        required_components = [
            'github_integration',
            'ai_services',
            'search_tools',
            'code_processing',
            'data_structures',
            'quantum_computation',
            'neural_processing',
            'terminal_orchestration',
            'unified_score'
        ]
        
        for component in required_components:
            assert component in unified, f"Missing component: {component}"
    
    def test_github_integration_active(self):
        """Test GitHub/Copilot integration"""
        orb = UnifiedOrb()
        result = orb.process("commit code")
        
        github = result['unified_result']['github_integration']
        assert github['status'] == 'integrated'
        assert github['copilot_active'] is True
    
    def test_ai_services_unified(self):
        """Test AI services (Claude, GPT, Hugging Face) are unified"""
        orb = UnifiedOrb()
        result = orb.process("explain quantum physics")
        
        ai = result['unified_result']['ai_services']
        assert ai['claude_code'] == 'active'
        assert ai['gpt_codex'] == 'active'
        assert ai['hugging_face_chat'] == 'active'
    
    def test_search_tools_integrated(self):
        """Test web and file search tools"""
        orb = UnifiedOrb()
        result = orb.process("search for documentation")
        
        search = result['unified_result']['search_tools']
        assert search['web_search'] == 'indexed'
        assert search['file_search'] == 'indexed'
    
    def test_data_structures_processing(self):
        """Test QR/barcode and API structure handling"""
        orb = UnifiedOrb()
        result = orb.process("encode this data")
        
        data_struct = result['unified_result']['data_structures']
        assert 'qr_code' in data_struct
        assert 'barcode' in data_struct
        assert data_struct['vacuoles'] == 'integrated'
    
    def test_quantum_computation_active(self):
        """Test quantum computing integration"""
        orb = UnifiedOrb()
        result = orb.process("quantum superposition")
        
        quantum = result['unified_result']['quantum_computation']
        assert quantum['qubits'] == 'active'
        assert quantum['ternary'] == 'active'
        assert quantum['binary'] == 'active'
        assert 'superposition' in quantum
    
    def test_neural_processing_active(self):
        """Test neural network processing"""
        orb = UnifiedOrb()
        result = orb.process("neural network test")
        
        neural = result['unified_result']['neural_processing']
        assert neural['neural_network'] == 'active'
        assert 'layer_output' in neural


class TestErrorHandling:
    """Test error handling and resilience"""
    
    def test_error_handling_unified(self):
        """Test that errors are handled gracefully"""
        orb = UnifiedOrb()
        
        # Force an error scenario
        result = orb._handle_error_unified(Exception("Test error"), "test input")
        
        assert result['state'] == 'resilient'
        assert result['unity_maintained'] is True
        unified = result['unified_result']
        assert unified['error_absorbed'] is True
        assert unified['null_power_active'] is True
    
    def test_fallback_processing(self):
        """Test fallback processing works"""
        orb = UnifiedOrb()
        fallback = orb._fallback_process("test data")
        
        assert fallback['input_acknowledged'] is True
        assert 'input_hash' in fallback
        assert fallback['processing_mode'] == 'safe_unified'


class TestUnityAndCohesion:
    """Test that the system maintains unity and cohesion"""
    
    def test_unity_score_calculation(self):
        """Test unity score is calculated"""
        orb = UnifiedOrb()
        score = orb._calculate_unity_score()
        
        assert 0.0 <= score <= 1.0
    
    def test_provenance_is_unified(self):
        """Test that provenance indicates unified processing"""
        orb = UnifiedOrb()
        result = orb.process("test")
        
        assert result['provenance'] == 'all_sources_simultaneously'
    
    def test_no_isolated_components(self):
        """Test that no component operates independently"""
        orb = UnifiedOrb()
        result = orb.process("simple test")
        
        # All components should be present even for simple input
        unified = result['unified_result']
        component_count = len([k for k in unified.keys() if k != 'unified_score'])
        assert component_count >= 8  # All major components
    
    def test_temporal_braid_integration(self):
        """Test temporal history is maintained"""
        orb = UnifiedOrb()
        
        orb.process("first input")
        orb.process("second input")
        orb.process("third input")
        
        assert len(orb.hyper_state.temporal_braid) == 3
    
    def test_self_compression(self):
        """Test self-compression reduces entropy"""
        orb = UnifiedOrb()
        
        initial_entropy = orb.hyper_state.entropy_metric
        orb.hyper_state.entropy_metric = 0.5
        
        orb.hyper_state.compress()
        
        assert orb.hyper_state.entropy_metric < 0.5


class TestHyperStateTensor:
    """Test the hyper-state tensor"""
    
    def test_tensor_initialization(self):
        """Test tensor initializes properly"""
        tensor = HyperStateTensor()
        
        assert isinstance(tensor.unified_state, dict)
        assert isinstance(tensor.quantum_registers, list)
        assert isinstance(tensor.temporal_braid, list)
    
    def test_tensor_compress(self):
        """Test tensor compression"""
        tensor = HyperStateTensor()
        tensor.entropy_metric = 1.0
        
        # Add many items to temporal braid
        for i in range(150):
            tensor.temporal_braid.append({'index': i})
        
        tensor.compress()
        
        assert tensor.entropy_metric < 1.0
        assert len(tensor.temporal_braid) == 100  # Limited to 100


class TestOrbConvenienceFunctions:
    """Test convenience functions"""
    
    def test_orb_process_function(self):
        """Test the orb_process convenience function"""
        result = orb_process("test input")
        
        assert 'orb_signature' in result
        assert 'unified_result' in result
    
    def test_get_status(self):
        """Test getting Orb status"""
        orb = get_orb()
        status = orb.get_status()
        
        assert 'state' in status
        assert 'unity_score' in status
        assert 'quantum_registers' in status
        assert 'signature' in status


class TestQuantumEncoding:
    """Test quantum encoding"""
    
    def test_quantum_encoding(self):
        """Test quantum encoding of input"""
        orb = UnifiedOrb()
        quantum_states = orb._encode_quantum("test data")
        
        assert len(quantum_states) > 0
        assert all(isinstance(q, complex) for q in quantum_states)
    
    def test_vectorization(self):
        """Test input vectorization"""
        orb = UnifiedOrb()
        vector = orb._vectorize("test input")
        
        assert len(vector) == 256
        assert np.allclose(np.sum(vector), 1.0, atol=1e-5)


class TestMultipleInputTypes:
    """Test various input types are handled"""
    
    def test_string_input(self):
        """Test string input"""
        result = orb_process("Hello, Orb!")
        assert result['unified_result']['unified_score'] > 0
    
    def test_dict_input(self):
        """Test dictionary input"""
        result = orb_process({"message": "test", "value": 123})
        assert result['unified_result']['unified_score'] > 0
    
    def test_list_input(self):
        """Test list input"""
        result = orb_process([1, 2, 3, 4, 5])
        assert result['unified_result']['unified_score'] > 0
    
    def test_number_input(self):
        """Test number input"""
        result = orb_process(42)
        assert result['unified_result']['unified_score'] > 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
