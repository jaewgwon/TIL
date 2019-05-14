import React from 'react';
import { ScrollView } from 'react-native';

export class CardForTest extends React.Component {
    render () {
        return (
            <ScrollView style={styles.container}>
                <Text>Just for text..</Text>
            </ScrollView>
        );
    }
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
})